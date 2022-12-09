from github import Github
from github.Repository import Repository
from alive_progress import alive_bar, alive_it, config_handler
from grapheme.grapheme_property_group import LeafNode
from markdown2 import Markdown 
from bs4 import BeautifulSoup as bs
from project_card_html_maker import *
import re
# import os
# os.chdir(os.path.dirname(os.path.realpath(__file__)))


from github_token import get_github_token

README_FN = "README.md"
HEADER_PREFIXES = ["#"*n for n in range(1,7)]

# First create a Github instance:
# using an access token
github = Github(get_github_token())

# Then play with your Github objects:
# for repo in github.get_user().get_repos():
#     print(repo.get_contents("README.md").decoded_content)

config_handler.set_global(bar=None, spinner_length=10, spinner='dots_waves')

markdowner = Markdown()

def prettify_html(html : str) -> str:
    # make BeautifulSoup from string
    soup = bs(html, "html.parser")                
    # prettify the html
    prettyHTML = soup.prettify()   
    return "\n".join([" " * 4 * (len(l) - len(l.lstrip())) + l.lstrip() for l in prettyHTML.splitlines()])

def get_nonempty_lines(readme : str) -> str:
    lines = [l for l in readme.splitlines() if l.strip() != "<br>" and l.strip() != '']
    commented = False
    non_comment_lines = [] 
    for l in lines:
        if "<!--" in l:
            commented = True
        if not commented and l.strip()[:2] != "//":
            non_comment_lines.append(l)
        if commented and "-->" in l:
            commented = False
    return non_comment_lines

def read_file(repo : Repository, file_name : str) -> str: 
    result = None
    try:
        result = repo.get_contents(file_name).decoded_content.decode("utf-8")
    except:
        print("oops, no readme file found!")
    return result

def is_valid_project(repo):
    readme = read_file(repo, README_FN)
    return (readme != None and
        "## Project Metadata" in readme and
        not "# Boilerplate for Projects on GitHub" in readme and 
        ("<!-- ## Image Gallery" in readme or not "### Placeholder Image" in readme) and
        not "This is the boilerplate for all my personal projects on GitHub." in readme and 
        not "- This is the template boilerplate repository for all personal projects" in readme and 
        not "(Active, Inactive, Archived)" in readme and 
        not "(Concept, In Progress, Functional, Complete)" in readme and 
        not "Jan '00 - Present" in readme
    )

def get_position_priority(repo : Repository) -> int:
    readme_txt : str = read_file(repo, README_FN)
    return int(re.search("<!-- portfolio.alecwarren.com position priority = (.*?) \(-1 is lowest, 0 is default, 10 is highest\)", readme_txt).group(1) if "<!-- portfolio.alecwarren.com position priority" in readme_txt else 0)

def extract_readme_info(repo : Repository) -> dict[str, str]:
    project_info = {}
    project_info["name"] = repo.name
    project_info["url"] = "http://github.com/a-dubs/" + repo.name
    raw_readme : str = read_file(repo, README_FN)
    readme_lines : list[str] = get_nonempty_lines(raw_readme)
    
    # print("\n"*10)
    # print(repo.name)
    # print(raw_readme)
    # print(readme_lines)
    project_info["title"] = str([l for l in readme_lines if l.split()[0] == "#"][0].lstrip()[2:])
    header_indexes = [i for i in range(len(readme_lines)) if readme_lines[i].split()[0] in ["##", "#"]]  
    # print("header_indexes:",header_indexes)
    project_info["description"] = "\n".join(readme_lines[header_indexes[0]+1:header_indexes[1]])
    header_indexes = header_indexes[int(not "<!-- ## Image Gallery" in raw_readme):] + [len(readme_lines)]
    # print(header_indexes)
    for i in range(len(header_indexes) - 1):
        start_line_no = header_indexes[i]
        end_line_no = header_indexes[i+1]
        section_name = str(readme_lines[start_line_no].lstrip()[3:]).lower().strip()
        section_content = "\n".join(readme_lines[start_line_no+1:end_line_no])
        project_info[section_name] = section_content

    metadata = {}
    for line in project_info["project metadata"].splitlines():
        if line.strip() != "":
            k = str(line.split(":")[0]).strip("* ").lower()
            v = str(line.split(":")[1]).strip("* ")
            metadata[k] = v
    project_info["metadata"] = metadata
    
    # image_gallery = None
    if "image gallery" in project_info and "### Placeholder Image" not in project_info["image gallery"]:
        image_gallery = []
        for line in project_info["image gallery"].splitlines():
            if line.strip().split()[0] == "###":
                caption = line[4:]
            if line[:2] == "![":
                alt_text = (line[2:line.find("]")]).strip()
                image_url = line[line.rfind("https://github") : line.rfind(")")]
                image_url = image_url.replace("https://github.com", "https://raw.githubusercontent.com").replace("/blob/","/")
                image_file_name = (line[line.rfind("/image_gallery/")+len("/image_gallery/") : line.rfind(")")]).strip()
                image_gallery.append({
                    "caption" : caption,
                    "alt_text" : alt_text,
                    "image_file_name" : image_file_name,
                    "image_file_path" : project_info["name"] + "/image_gallery/" + image_file_name,
                    "image_url" : image_url
                }) 
        project_info["image gallery"] = image_gallery

    project_info["summary"] = prettify_html(markdowner.convert(project_info["summary"]).encode("utf-8").decode("utf-8"))

    return project_info

def main():
        
    repos = list(github.get_user().get_repos())

    # get list of all project repos
    projects = [repo for repo in alive_it(repos) if is_valid_project(repo)]

    all_project_cards_html = ""

    projects.sort(key=get_position_priority, reverse=True)
    print(f"{len(projects)} valid projects found for portfolio!")
    print([repo.name for repo in projects])

    project_infos = {}
    for repo in projects:
        project_infos[repo.name] = extract_readme_info(repo)
        # if image gallery has more than 1 image, assume repo's readme has been populated and is ready to be added to site
        all_project_cards_html += "\n" + prettify_html(make_project_card(project_infos[repo.name])) + "\n"
    
    full_html_output = ""
    with open("index.html", mode="r") as html_file:
        lines = html_file.readlines()
        start_line_no = [lines.index(l) + 2 for l in lines if  "AUTO GENERATED PROJECT CARDS BELOW" in l][0]
        stop_line_no = [lines.index(l) - 2 for l in lines if  "AUTO GENERATED PROJECT CARDS ABOVE" in l][0]
        full_html_output = "".join(
            lines[: start_line_no] + 
            ["\n\n"] + 
            ["        " + l for l in all_project_cards_html.splitlines(keepends=True)] + 
            ["\n\n\n"] + 
            lines[stop_line_no + 1 :]
        )


    # with open("testing autofill index.html", mode="w") as html_file:
    with open("index.html", mode="w") as html_file:
        html_file.write(full_html_output)

main()

# print(get_nonempty_lines("abc \n\
# <!-- ## Image Gallery \n\
# \n\
# ### Placeholder Image (This is the image's caption/label) \n\
# ![Please end my suffering... (This is the image's alt text)](https://github.com/a-dubs/github-project-template/blob/master/image_gallery/Please_replace_me_I_am_begging_you.jpg) \n\
# <br> --> \n\
# 123\n"))