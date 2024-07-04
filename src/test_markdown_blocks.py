import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node
)

class TestHTMLNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
            markdown = """# This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

    * This is a list item
    * This is another list item"""
            blocks = markdown_to_blocks(markdown)
            self.assertEqual(blocks, ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is a list item\n    * This is another list item"])
            
            markdown = """This is **bolded** paragraph

    This is another paragraph with *italic* text and `code` here
    This is the same paragraph on a new line

    * This is a list
    * with items"""
            blocks = markdown_to_blocks(markdown)
            self.assertEqual(blocks, ["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\n    This is the same paragraph on a new line", "* This is a list\n    * with items"])
            
    
    def test_block_to_block_type(self):
        
        markdown = """# This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n
    
    ```This is a paragraph of text. It has some **bold** and *italic* words inside of it.```\n
    
    > Quote
    > Quote
    > Quote

    * This is a list item
    * This is another list item"""
        blocks = markdown_to_blocks(markdown)
        blocks_types = []
        for block in blocks:
            blocks_types.append(block_to_block_type(block))
        self.assertEqual(blocks_types, ["heading", "paragraph", "code", "quote", "unordered_list"])
        
        markdown = """This is **bolded** paragraph

    This is another paragraph with *italic* text and `code` here
    This is the same paragraph on a new line

    * This is a list
    * with items"""
        blocks = markdown_to_blocks(markdown)
        blocks_types = []
        for block in blocks:
            blocks_types.append(block_to_block_type(block))
            
        self.assertEqual(blocks_types, ["paragraph", "paragraph", "unordered_list"])
    
    def test_markdown_to_html_node(self):
        markdown = """# This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n
    
    ```This is a paragraph of text. It has some **bold** and *italic* words inside of it.```\n
    
    ```
    This is a paragraph of text. 
    It has some **bold** and *italic* words inside of it.
    ```\n
    
    > Quote
    > Quote
    > Quote

    * This is a list item
    * This is another list item"""
        html_nodes = markdown_to_html_node(markdown)
        print(html_nodes)
        #html = html_nodes.to_html()
        #print(html)