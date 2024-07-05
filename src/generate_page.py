import os

from markdown_blocks import (
    markdown_to_html_node,
)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

def generate_page_recursive(content_path, static_path, template_path, dest_path): 
    markdown = ""
    template = ""
    with open(template_path) as t:
        template = t.read()
        t.close()
    for file_md in os.listdir(content_path):
        if os.path.isfile(content_path + '/' + file_md):
            with open(content_path+"/"+'index.md') as f:
                markdown = f.read()
                f.close()

            node = markdown_to_html_node(markdown)
            html = node.to_html()
            
            title = extract_title(markdown)
            template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
        
            with open(dest_path + '/' + 'index.html', 'w+') as f:
                print(template, file=f)
                f.close()
        else:
            os.mkdir(dest_path + '/' + file_md)
            generate_page_recursive(content_path + '/' + file_md, static_path, template_path, dest_path + '/' + file_md)
