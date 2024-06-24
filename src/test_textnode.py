import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)
        
    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)
    
    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This isnt a bold node", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a link node", text_type_link, "https://www.boot.dev")
        node2 = TextNode("This is a link node", text_type_link, "https://www.boot.dev")
        self.assertEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a link node", text_type_link, "https://www.boot.dev")
        self.assertEqual(repr(node), "TextNode(This is a link node, link, https://www.boot.dev)")
    
    # def test_text_node_to_html(self):
    #     node_text = TextNode("This is a text node", text_type_text)
    #     node_bold = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
    #     node_link = TextNode("This is a text node", text_type_link, "https://www.boot.dev")
    #     node_img = TextNode("This is a text node", text_type_image, "https://www.boot.dev")
    #     self.assertEqual(text_node_to_html_node(node_text), "This is a text node")
    #     self.assertEqual(text_node_to_html_node(node_bold), "<b>This is a text node</b>")
    #     self.assertEqual(text_node_to_html_node(node_link), '<a href="https://www.boot.dev">This is a text node</a>')
    #     self.assertEqual(text_node_to_html_node(node_img), '<img src="https://www.boot.dev" alt="This is a text node"></img>')

if __name__ == "__main__":
    unittest.main()