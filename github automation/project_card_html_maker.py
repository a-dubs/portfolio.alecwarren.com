from os.path import exists
import os
import urllib.request
from alive_progress import alive_bar, alive_it
import difflib

c2a_exceptions = {
    # "ndw.com" : {"text" : "Visit NexusDesignWorks.com", "hyperlink" : "https://nexusdesignworks.com"}
}

def make_c2a_button(pi : dict[str, str]):
    hyperlink = pi["url"] if not pi["name"] in c2a_exceptions else c2a_exceptions[pi["name"]]["hyperlink"]
    c2a_text = 'See Full Project on GitHub' if not pi["name"] in c2a_exceptions else c2a_exceptions[pi["name"]]["text"]
    return (
        '            <div id="c2a" class="btn btn-dark"><a target="_blank" href="' + hyperlink + '">\n' + \
        '                ' + c2a_text + '\n' + \
        '            </a></div>\n' 
    )
# def get_pythonic_string_of_html():
#     return "\n".join(["'" + l + "' \\n + \\" for l in raw_project_card_html.replace("'","\\'").splitlines()])

def make_slide_html(image_info : dict[str, str]) -> str:
    download_image_from_github(image_info["image_url"], 'projects/' + image_info["image_file_path"])
    return (
'                    <li class="slide">\n' + \
'                        <h3 class="caption h-center-a">\n' + \
'                            <div>' + image_info["caption"] + '</div>\n' + \
'                        </h3>\n' + \
'                        <div class="content cov"\n' + \
'                            style="background-image: url(\'projects/' + image_info["image_file_path"] + '\');">\n' + \
'                        </div>\n' + \
'                    </li>\n'
)

def make_project_metadata(project_info):
    status_class_names = ["active", "inactive", "archived"]
    status_labels = ["Active", "Inactive", "Archived"]
    progress_class_names = ["concept", "in-progress", "functional", "complete"]
    progress_labels = ["Concept", "In-Progress", "Functional", "Complete"]
    status_given = project_info["metadata"]["project status"].strip().lower().replace(" ","-")
    progress_given = project_info["metadata"]["project progress"].strip().lower().replace(" ","-")
    status_class = difflib.get_close_matches(status_given, status_class_names)[0]
    status_label = status_labels[status_class_names.index(status_class)]
    progress_class = difflib.get_close_matches(progress_given, progress_class_names)[0]
    progress_label = progress_labels[progress_class_names.index(progress_class)]
    return (
    '    <div class="metadata row justify-content-center g-0">\n' + \
    '        <div class="data dates col-24 col-md">\n' + \
    '            Dates: ' + project_info["metadata"]["project dates"] + \
    '        </div>\n' + \
    '        <div class="data status-' + status_class + ' col-24 col-md">\n' + \
    '            Status: ' + status_label + \
    '        </div>\n' + \
    '        <div class="data progress-' + progress_class + ' col-24 col-md">\n' + \
    '            Progress: ' + progress_label + \
    '        </div>\n' + \
    '    </div>\n'
    )

def make_project_card(project_info : dict[str, str]) -> str:
    pi = project_info
    add_gallery_javascript(pi["name"])
    print("\n\n")
    print(pi)   
    print("\n\n")
    return (
    '<div id="' + pi["name"] +'" class="container project">\n' + \
    '\n' + \
        make_project_metadata(pi) + \
    '    <div class="collapse-area">\n' + \
    '        <div class="row justify-content-between g-0">\n' + \
    '            <div class="header-container col-22 offset-1">\n' + \
    '                <h3 class="title"> ' + pi["title"] + \
    '                <h4 class="description"> \n' + \
    '                    ' + pi["description"] + \
    '                </h4>\n' + \
    '            </div>\n' + \
    '        </div>\n' + \
    '        <div class="button-container row justify-content-center">\n' + \
    '            <div class="expand-btn btn btn-outline-dark " data-bs-toggle="collapse"\n' + \
    '                data-bs-target="#collapser-' + pi["name"] + '">\n' + \
    '                <p>&nbsp;Expand&nbsp;</p>\n' + \
    '            </div>\n' + \
    '        </div>\n' + \
    '    </div>\n' + \
    '\n' + \
    '    <div id="collapser-' + pi["name"] + '" class="collapser collapse">\n' + \
    '        <div class="expand-area row g-0 justify-content-center align-items-center">\n' + \
    '            <script src="projects/' + pi["name"] + '/' + pi["name"] + '-gallery-script.js"></script>\n' + \
    '            <div id="' + pi["name"].replace("-","_") + \
    '_gallery" class="gallery col-24 col-sm-20 col-md-18 col-lg-11">\n' + \
    '                <ul id="carousel">\n' + \
                        "\n".join([make_slide_html(image_info) for image_info in alive_it(pi["image gallery"])]) + '\n' + \
    '                </ul>\n' + \
    '                <div id="left" class="gallery-btn notselected"> <img\n' + \
    '                        src="l-cheveron.png"\n' + \
    '                        class="vert_spacer" id="icon" />\n' + \
    '                    <div class="icon_bg"></div>\n' + \
    '                </div>\n' + \
    '                <div id="right" class="gallery-btn notselected"><img\n' + \
    '                        src="r-chevron.png"\n' + \
    '                        class="vert_spacer" id="icon" />\n' + \
    '                    <div class="icon_bg"></div>\n' + \
    '                </div>\n' + \
    '                <div class="island" id="bar_island">\n' + \
    '                    <ul id="bar_island_ul"></ul>\n' + \
    '                </div>\n' + \
    '            </div>\n' + \
    '\n' + \
    '            <div class="summary col-22 col-sm-19 col-md-17 col-lg-11">\n' + \
    '                <h3>Summary</h3>\n' + \
                        pi["summary"] + '\n' + \
    '            </div>\n' + \
                 make_c2a_button(pi) + \
    '            <div class="col-24 secondary-collapse-btn" data-bs-toggle="collapse"\n' + \
    '            data-bs-target="#collapser-' + pi["name"] + '">\n' + \
    '                <div class="txt-box">\n' + \
    '                    Collapse\n' + \
    '                    <div class="bg h-center-a"></div>\n' + \
    '                </div>\n' + \
    '            </div>\n' + \
    '        </div>\n' + \
    '    </div>\n' + \
    '</div>\n' 
    )

def make_project_folder_if_needed(project_name):
    if not exists('projects/' + project_name):
        os.makedirs('projects/' + project_name)

    if not exists('projects/' + project_name  + '/image_gallery'):
        os.makedirs('projects/' + project_name  + '/image_gallery')

def add_gallery_javascript(project_name):
    make_project_folder_if_needed(project_name)
    gallery_name = project_name.replace("-","_") + "_gallery"
    gallery_script_result = ""
    with open("GalleryName-gallery-script.js", "r") as template_js_file:
        gallery_script_result = "".join(template_js_file.readlines())
        gallery_script_result = gallery_script_result.replace("GalleryName()", gallery_name + "()")
        gallery_script_result = gallery_script_result.replace("GalleryName", gallery_name)
    
    with open("projects/" + project_name + "/" + project_name + "-gallery-script.js", "w") as output_js_file:
        output_js_file.write(gallery_script_result)

def download_image_from_github(download_url, local_file_path):
    try: 
        return urllib.request.urlretrieve(download_url, local_file_path)
    except:
        return None

# print(get_pythonic_string_of_html())



