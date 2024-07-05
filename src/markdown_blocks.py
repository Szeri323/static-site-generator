from htmlnode import (ParentNode)
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    try:
        for block in blocks:
            if block.startswith('#'):
                counter = 0
                for char in block:
                    if char == "#":
                        counter += 1
                if counter == 1:        
                    return block.lstrip('# ')
                else:
                    raise Exception("Markdown does not contain h1")
    except Exception as e:
        print(e)
        

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        child = block_to_html_node(block)
        children.append(child)
    return ParentNode("div", children)
    
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    if block_type == block_type_unordered_list:
        return unordered_list_to_html_node(block)
    if block_type == block_type_ordered_list:
        return ordered_list_to_html_node(block)
    raise ValueError("Invalid block type")



def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n") 
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split('\n')
    filtred_lines = []
    for line in lines:
        line = line.strip()
        filtred_lines.append(line)
        
    if len(filtred_lines) > 1:
        other_lines_sign_check = True
        if filtred_lines[0].startswith('>'):
            for line in filtred_lines:
                if line.startswith('>'):
                    pass
                else:
                    other_lines_sign_check = False
            if other_lines_sign_check:
                return block_type_quote
        if filtred_lines[0].startswith('* '):
            for line in filtred_lines:
                if line.startswith('* '):
                    pass
                else:
                    other_lines_sign_check = False
            if other_lines_sign_check:
                return block_type_unordered_list
        if filtred_lines[0].startswith('- '):
            for line in filtred_lines:
                if line.startswith('- '):
                    pass
                else:
                    other_lines_sign_check = False
            if other_lines_sign_check:
                return block_type_unordered_list
        if filtred_lines[0].startswith('1.'):
            for i in range(len(filtred_lines)):
                if filtred_lines[i].startswith(f'{i+1}.'):
                    pass
                else:
                    other_lines_sign_check = False
            if other_lines_sign_check:
                return block_type_ordered_list
    
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    
    if block.startswith('```') and block.endswith('```'):
        return block_type_code
    
    else:
        return block_type_paragraph
    

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split('\n')
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f'h{level}', children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split('\n')
    new_lines = []
    for line in lines:
        line = line.strip()
        if not line.startswith('>'):
            raise ValueError("Invalid quote block")
        new_lines.append(line.strip(">").strip())
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block):
    lines = block.split('\n')
    html_items = []
    for line in lines:
        line = line.strip()
        if line.startswith('*') or line.startswith('-'):
            text = line[2:]
            children = text_to_children(text)
            html_items.append(ParentNode("li", children))
        else:
            raise ValueError("Invalid list block")
    return ParentNode("ul", html_items)

def ordered_list_to_html_node(block):
    lines = block.split('\n')
    html_items = []
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        if not lines[i].startswith(f'{i+1}.'):
            raise ValueError("Invalid list block")
        text = lines[i][3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    
    
    return ParentNode("ol", html_items)
