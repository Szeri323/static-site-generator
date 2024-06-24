import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    texts = []
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        texts = node.text.split(delimiter)
        if texts[-1:] == [""]:
            texts.pop()
        for i in range(len(texts)):
            if texts[0] == "":
                if i == 0:
                    continue
            if i % 2 != 0:
                new_nodes.append(TextNode(texts[i], text_type))
            else:
                new_nodes.append(TextNode(texts[i], text_type_text))
        return new_nodes
    
def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches =  re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches =  re.findall(pattern, text)
    return matches