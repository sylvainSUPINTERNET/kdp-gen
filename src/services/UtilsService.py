import os
from mako.template import Template
import shutil

from src.constants.constants import OUTPUT_FOLDER, TEMPLATE_FILE

def copy_template_to_chapter_page(page_chapter_name:str) -> str:

    """
        Take xhtml template and copy it into output ( to create a new ebook page ) and return the path of the new file created
    """

    src:str = os.path.abspath(TEMPLATE_FILE)
    dst:str = os.path.join(os.path.abspath(OUTPUT_FOLDER), f"{page_chapter_name}.xhtml")

    shutil.copy(src, dst)

    return dst

def write_to_page(page_chapter_file_path:str, corpus:str, img_path:str="./img_generation/default.jpeg") -> str :

    """
        Read the chapter page xhtml and populate the variable
    """

    data = {
        "text":f"{corpus}",
        "illustration_path":f"{img_path}"
    }
    
    with open(page_chapter_file_path, 'r') as f:
        template_str = f.read()

    # Create a Mako template object
    template = Template(template_str)
    # Render the data in the template and print the resulting HTML
    html_output = template.render(**data)

    # Write new HTML generated with variables populated to the xhtml ( page of chapter )
    with open(page_chapter_file_path, "w", encoding="utf-8") as f:
        f.write(html_output)

    return html_output


