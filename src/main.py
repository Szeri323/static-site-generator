from copy_from_to import copy_from_to_recursive
from generate_page import generate_page_recursive

def main():
    content_path = '/home/szeri/git/boot.dev/static-site-generator/content'
    static_path = '/home/szeri/git/boot.dev/static-site-generator/static'
    template_path = '/home/szeri/git/boot.dev/static-site-generator/html_templates/template.html'
    dest_path = '/home/szeri/git/boot.dev/static-site-generator/public'
    print(f'Generating page from {content_path} to {dest_path} using {template_path}')
    copy_from_to_recursive(static_path, dest_path)
    generate_page_recursive(content_path, static_path, template_path, dest_path)
    print(f'Generating done')
    
main()