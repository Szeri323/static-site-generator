from copy_from_to import copy_from_to_recursive
from generate_page import generate_page_recursive
from sys import platform
import os

def main():
    path_sign = '/'
    if platform == "win32":
        path_sign = '\\'

    print(platform)
    print(os.getcwd().replace(path_sign+'src', path_sign+'content'))
    content_path = os.getcwd().replace(path_sign+'src', path_sign+'content')
    static_path = os.getcwd().replace(path_sign+'src', path_sign+'static')
    template_path = os.getcwd().replace(path_sign+'src', path_sign+'html_templates' + path_sign + 'template.html')
    dest_path = os.getcwd().replace(path_sign+'src', path_sign+'public')
    print(f'Generating page from {content_path} to {dest_path} using {template_path}')
    copy_from_to_recursive(static_path, dest_path)
    generate_page_recursive(content_path, content_path, static_path, template_path, dest_path)
    print(f'Generating done')
    
main()