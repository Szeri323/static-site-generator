from markdown_blocks import (
    markdown_to_html_node,
    extract_title
)
from copy_from_to import copy_from_to

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    markdown = ""
    template = ""
    with open(from_path+"/"+'index.md') as f:
        markdown = f.read()
        f.close()
    with open(template_path) as t:
        template = t.read()
        t.close()
        
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    copy_from_to(from_path, dest_path)
    with open(dest_path + '/' + 'index.html', 'w+') as f:
        print(template, file=f)
        f.close()
        
        
def main():
    from_path = '/home/szeri/git/boot.dev/static-site-generator/content'
    template_path = '/home/szeri/git/boot.dev/static-site-generator/html_templates/template.html'
    dest_path = '/home/szeri/git/boot.dev/static-site-generator/public'
    generate_page(from_path, template_path, dest_path)
    
if __name__ == "__main__":
    main()