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

def generate_page_recursive(ansolute_content_path, content_path, static_path, template_path, dest_path): 
    markdown = ""
    template = ""
    for file_md in os.listdir(content_path):

        with open(template_path) as t:
            template = t.read()
            t.close()

        if os.path.isfile(content_path + '/' + file_md):
            with open(content_path+"/"+file_md) as f:
                markdown = f.read()
                f.close()

            node = markdown_to_html_node(markdown)
            html = node.to_html()
            
            title = extract_title(markdown)

            depth_of_file = content_path.replace(ansolute_content_path, '')

            counter = depth_of_file.split('/')
            if len(counter) == 1:
                template = template.replace("{{ Style }}", './index.css')
            else :
                template = template.replace("{{ Style }}", '../' * (len(counter) - 1) + 'index.css')

            template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)


            file_html = file_md.replace('.md','.html')

            with open(dest_path + '/' + file_html, 'w+') as f:
                print(template, file=f)
                f.close()
        else:
            os.mkdir(dest_path + '/' + file_md)
            generate_page_recursive(ansolute_content_path, content_path + '/' + file_md, static_path, template_path, dest_path + '/' + file_md)
