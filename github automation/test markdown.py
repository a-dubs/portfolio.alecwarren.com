# root = lh.tostring(sliderRoot) #convert the generated HTML to a string
from markdown2 import Markdown 

md = "## Summary  \n- Fully modified my cheap yet surprisingly reliable 75% RGB mechanical keyboard.  \n- Transfered the o-rings from the old keycaps to the new blank fog-white transluscent keycaps.  \n"

markdowner = Markdown()

print(markdowner.convert(md))

# html = "<ul>\n<li>This is the template boilerplate repository for all personal projects that I have on my GitHub.</li>\n<li>This template will expedite the creation and maintenance of all my various projects' repositories.</li>\n<li>And more importantly, the standardized format will allow for auto parsing of the repository by a python script to automatically update my personal portfolio website.</li>\n</ul>\n"


