import os

from markdown_blocks import (
    markdown_to_html_node,
)

from generate_navigation import generate_navigation

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
            with open(content_path+"/"+file_md, encoding="utf-8") as f:
                markdown = f.read()
                f.close()
            node = markdown_to_html_node(markdown)
            html = node.to_html()
            
            title = extract_title(markdown)

            depth_of_file = content_path.replace(ansolute_content_path, '')

            counter = depth_of_file.split('/')
            
            static_files_list = os.listdir(static_path)
            style_file_name = ""
            for file_name in static_files_list:
                if os.path.isfile(static_path + '/' + file_name) and '.css' in file_name:
                    style_file_name = file_name
            
            if len(counter) == 1:
                template = template.replace("{{ Style }}", f'./{style_file_name}')
            else :
                template = template.replace("{{ Style }}", '../' * (len(counter) - 1) + style_file_name)

            template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
            
            template = generate_navigation(counter, template)

            file_html = file_md.replace('.md','.html')

            with open(dest_path + '/' + file_html, 'w+', encoding="utf-8") as f:
                print(template, file=f)
                f.close()
        else:
            os.mkdir(dest_path + '/' + file_md)
            generate_page_recursive(ansolute_content_path, content_path + '/' + file_md, static_path, template_path, dest_path + '/' + file_md)
