import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode(props={"href": "https://x"})
        self.assertEqual(node.props_to_html(), ' href="https://x"')

    def test_multiple_props(self):
        node = HTMLNode(props={"href": "https://x", "target": "_blank"})
        got = node.props_to_html()
        
        self.assertIn(' href="https://x"', got)
        self.assertIn(' target="_blank"', got)
        self.assertEqual(len(got.split()), 2)  

if __name__ == "__main__":
    unittest.main()
