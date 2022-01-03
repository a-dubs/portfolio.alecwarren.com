from github import Github
from github.Repository import Repository
from alive_progress import alive_bar, alive_it, config_handler
from markdown2 import Markdown
markdowner = Markdown()

README_FN = "README.md"
HEADER_PREFIXES = ["#"*n for n in range(1,7)]
print("header_prefixes:", HEADER_PREFIXES)

# First create a Github instance:
# using an access token
github = Github("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")

# Then play with your Github objects:
# for repo in github.get_user().get_repos():
#     print(repo.get_contents("README.md").decoded_content)

config_handler.set_global(bar=None, spinner_length=10, spinner='dots_waves')

def get_nonempty_lines(readme : str) -> str:
    return [l for l in readme.splitlines() if not "<br>" in l and l != '']

def read_file(repo : Repository, file_name : str) -> str: 
    return repo.get_contents(file_name).decoded_content.decode("utf-8")

def is_project(repo):
    readme = read_file(repo, README_FN)
    return "## Project Meta-Data" in readme

def extract_readme_info(repo : Repository) -> dict[str, str]:
    project_info = {}
    project_info["name"] = repo.name
    project_info["url"] = "https://github.com/a-dubs/" + repo.name
    raw_readme : str = read_file(repo, README_FN)
    readme_lines : list[str] = get_nonempty_lines(raw_readme)
    print(readme_lines)
    project_info["title"] = str([l for l in readme_lines if l.split()[0] == "#"][0].lstrip()[2:])
    header_indexes = [i for i in range(len(readme_lines)) if readme_lines[i].split()[0] in ["##", "#"]]  
    project_info["description"] = "\n".join(readme_lines[header_indexes[0]+1:header_indexes[1]])
    header_indexes = header_indexes[2:] + [len(readme_lines)]
    print(header_indexes)
    for i in range(len(header_indexes)-1):
        start_line_no = header_indexes[i]
        end_line_no = header_indexes[i+1]
        section_name = str(readme_lines[start_line_no].lstrip()[3:]).lower()
        section_content = "\n".join(readme_lines[start_line_no+1:end_line_no])
        project_info[section_name] = section_content

    print(project_info)
    for key in project_info:
        metadata = {}
        if "meta-data" in key or "metadata" in key or "meta data" in key:
            for line in project_info[key].splitlines():
                if line.strip() != "":
                    k = str(line.split(":")[0]).strip("* ")
                    v = str(line.split(":")[1]).strip("* ")
                    metadata[k] = v
            project_info[key] = metadata
            break
    return project_info
    
def make_html(readme_info : dict[str, str]) -> str:
    pass

# get list of all project repos
projects = [repo for repo in alive_it(github.get_user().get_repos()) if is_project(repo)]



# get name
for repo in projects:
    print(extract_readme_info(repo))

