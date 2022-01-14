from os.path import exists
import os
import urllib.request
from alive_progress import alive_bar, alive_it
import difflib

raw_project_card_html = """
<div id="project-nexus-website" class="container project">

    <div class="metadata row justify-content-center g-0">
        <div class="data bg-secondary text-light col-24 col-md">
            Dates: Nov '16 - Present
        </div>
        <div class="data bg-primary text-light col-24 col-md">
            Status: Active
        </div>
        <div class="data bg-success text-light col-24 col-md">
            Progress: Functional
        </div>
    </div>
    <div class="collapse-area">
        <div class="row justify-content-between g-0">
            <div class="header-container col-22 offset-1">
                <div style="background-image: url('');" class="img thumbnail"></div>
                <h3 class="title"> Think Nexus Design Website </h3>
                <h4 class="description"> 
                    Commercial Website Developed From Scratch using HTML, CSS, and
                    JavaScript with jQuery 
                </h4>
            </div>
        </div>
        <div class="button-container row justify-content-center">
            <div class="expand-btn btn btn-outline-dark " data-bs-toggle="collapse"
                data-bs-target="#collapser-nexus-website">
                &nbsp;Expand&nbsp;
            </div>
        </div>
    </div>

    <div id="collapser-nexus-website" class="collapser collapse">
        <div class="expand-area row g-0 justify-content-center ">
            <script src="gallery-nexus-website-script.js"></script>
            <div id="nexus_website_gallery" class="gallery col-24 col-sm-20 col-md-18 col-lg-11">
                <ul id="carousel">
                    <li class="slide">
                        <h3 class="caption h-center-a">
                            <div> home page</div>
                        </h3>
                        <div class="content cov"
                            style="background-image: url('projects/nexus-website/home.JPG');">
                        </div>
                    </li>
                    <li class="slide">
                        <h3 class="caption h-center-a">
                            <div> services page</div>
                        </h3>
                        <div class="content cov"
                            style="background-image: url('projects/nexus-website/services.JPG');">
                        </div>
                    </li>
                    <li class="slide">
                        <h3 class="caption h-center-a">
                            <div> individual services page</div>
                        </h3>
                        <div class="content cov"
                            style="background-image: url('projects/nexus-website/individual-service.JPG');">
                        </div>
                    </li>
                    <li class="slide">
                        <h3 class="caption h-center-a">
                            <div> projects page </div>
                        </h3>
                        <div class="content cov"
                            style="background-image: url('projects/nexus-website/projects.JPG');">
                        </div>
                    </li>
                    <li class="slide">
                        <h3 class="caption h-center-a">
                            <div> services page </div>
                        </h3>
                        <div class="content cov"
                            style="background-image: url('projects/nexus-website/about.JPG');">
                        </div>
                    </li>
                    <li class="slide">
                        <h3 class="caption h-center-a">
                            <div> contact page </div>
                        </h3>
                        <div class="content cov"
                            style="background-image: url('projects/nexus-website/contact.JPG');">
                        </div>
                    </li>
                    <li class="slide">
                        <h3 class="caption h-center-a">
                            <div> custom location map </div>
                        </h3>
                        <div class="content cov"
                            style="background-image: url('projects/nexus-website/contact-map.JPG');">
                        </div>
                    </li>

                </ul>
                <div id="left" class="gallery-btn notselected"> <img
                        src="l-cheveron.png"
                        class="vert_spacer" id="icon" />
                    <div class="icon_bg"></div>
                </div>
                <div id="right" class="gallery-btn notselected"><img
                        src="r-chevron.png"
                        class="vert_spacer" id="icon" />
                    <div class="icon_bg"></div>
                </div>
                <div class="island" id="bar_island">
                    <ul id="bar_island_ul"></ul>
                </div>
            </div>

            <div class="summary col-22 col-sm-19 col-md-17 col-lg-11">
                <h3>Summary</h3>
                <ul>
                    <li> My first full-fledged website. First commercial website, first fully responsive
                        website, and first public website. </li>
                    
                        <ul>
                            <li> Developed from scratch using HTML, CSS, JavaScript, and jQuery. </li>
                            <li> Developed from scratch using HTML, CSS, JavaScript, and jQuery. </li>
                            <ul>
                                <li> Developed from scratch using HTML, CSS, JavaScript, and jQuery. </li>
                                <li> Developed from scratch using HTML, CSS, JavaScript, and jQuery. </li>
                            </ul> 
                        </ul>       
            
                    <li> Made website fully responsive using breakpoints for the four different general
                        categories of screen sizes: mobile, split screen, HD desktop, and Full-HD desktop. </li>
                    <li> Published initial site at the end of 2016 and have been slowly upgrading ever since.
                    </li>
                    <li>
                        Released major update, site V2.0, in 2019 giving the website a completely unique mobile
                        site layout, featuring an entirely different taskbar and footer from the desktop site.
                    </li>
                </ul>
            </div>
            <div id="c2a" class="btn btn-dark"><a target="_blank" href="http://ThinkNexusDesign.com">
                Visit ThinkNexusDesign
            </a></div>
            <div class="col-24 secondary-collapse-btn" data-bs-toggle="collapse"
            data-bs-target="#collapser-nexus-website">
                <div class="txt-box">
                    Collapse
                    <div class="bg h-center-a"></div>
                </div>
            </div>
        </div>
    </div>
</div>
"""


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
def get_pythonic_string_of_html():
    return "\n".join(["'" + l + "' \\n + \\" for l in raw_project_card_html.replace("'","\\'").splitlines()])

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
    status_given = project_info["metadata"]["project status"].lower().replace(" ","-")
    progress_given = project_info["metadata"]["project progress"].lower().replace(" ","-")
    status_class = difflib.get_close_matches(status_given, status_class_names)[0]
    status_label = difflib.get_close_matches(status_given, status_labels)[0]
    progress_class = difflib.get_close_matches(progress_given, progress_class_names)[0]
    progress_label = difflib.get_close_matches(progress_given, progress_labels)[0]
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
    '                &nbsp;Expand&nbsp;\n' + \
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



