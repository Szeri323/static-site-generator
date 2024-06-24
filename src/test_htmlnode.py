import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode(
            "p", 
            "hello world", 
            None, 
            {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "hello world")
        self.assertEqual(node.to_html(), '<p>hello world</p>')
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), 'This is a paragraph of text.')
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "hello world")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><span>hello world</span></div>')   
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><span><b>grandchild</b></span></div>')
    
    
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")
    
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(node.to_html(), "<h2><b>Bold text</b>Normal text<i>Italic text</i>Normal text</h2>")
    
    # First tests
        
    # def test_to_html_one_child(self):
    #     node = ParentNode("p", [LeafNode("b", "Bold text")])
    #     self.assertEqual(node.to_html(), "<p><b>Bold text</b></p>")
        
    # def test_to_html_one_parent_one_child(self):
    #     node = ParentNode("p", [ParentNode("p", [LeafNode("b", "Bold text")]),LeafNode("b", "Bold text")])
    #     self.assertEqual(node.to_html(), "<p><p><b>Bold text</b></p><b>Bold text</b></p>")
    
    # def test_to_html_many_parents_many_children(self):
    #     node = ParentNode(
    #         "p", [
    #             ParentNode(
    #                 "p", [
    #                     ParentNode(
    #                         "p", [
    #                             LeafNode("i", "Italic text", {"href": "https://www.google.com", "target": "_blank"})
    #                             ]
    #                         ),
    #                     LeafNode("b", "Bold text"), 
    #                     LeafNode("i", "Italic text")
    #                     ]
    #                 ),
    #             LeafNode("b", "Bold text"),
    #             ParentNode(
    #                 "p", [
    #                     LeafNode("i", "Italic text")
    #                     ]
    #                 ),
    #             LeafNode("b", "Bold text")
    #             ]
    #         )
    #     self.assertEqual(
    #         node.to_html(), 
    #         '<p><p><p><i href="https://www.google.com" target="_blank">Italic text</i></p><b>Bold text</b><i>Italic text</i></p><b>Bold text</b><p><i>Italic text</i></p><b>Bold text</b></p>'
    #         )

if __name__=="__main__":
    unittest.main()
