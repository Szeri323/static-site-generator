import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, '**', text_type_bold)
    nodes = split_nodes_delimiter(nodes, '*', text_type_italic)
    nodes = split_nodes_delimiter(nodes, '`', text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        texts = []
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
    
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        image_tuple = extract_markdown_images(node.text)
        remaining_text = node.text
        
        if len(image_tuple) == 0:
            new_nodes.append(node)
            continue
        
        for alt_text, url in image_tuple:
            parts = remaining_text.split(f'![{alt_text}]({url})', 1)
            
            if len(parts) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            
            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text))
                
            new_nodes.append(TextNode(alt_text, text_type_image, url))
            
            remaining_text = parts[1]
            
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, text_type_text))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        links_tuple = extract_markdown_links(node.text)

        
        for link in links_tuple:
            parts = remaining_text.split(f'[{link[0]}]({link[1]})',1)
            
            if parts[0]:
                new_nodes.append(TextNode(parts[0],text_type_text,None))
            
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            
            remaining_text = parts[1]

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, text_type_text))    
                 
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches =  re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches =  re.findall(pattern, text)
    return matches