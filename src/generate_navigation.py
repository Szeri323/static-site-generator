import os


def generate_navigation(content_path, file_tree, counter, template):
    print("In generate navigation")
    print(content_path)
    print(file_tree)
    print(len(counter))
    if len(counter) == 1:
        template = template.replace("{{ Navigation }}", './')
    else :
        template = template.replace("{{ Navigation }}", '../' * (len(counter) - 1) + '')
    print(template)
    print("End")