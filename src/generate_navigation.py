import os


def generate_navigation(content_path, file_tree, counter, template):
    if len(counter) == 1:
        template = template.replace("{{ Navigation }}", './')
    else :
        template = template.replace("{{ Navigation }}", '../' * (len(counter) - 1) + '')
    return template