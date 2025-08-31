import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_noteq(self):
        node1 = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_eq_type(self):
        node1 = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node1, node2)

    def test_noteq_type_diff(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_eq_with_url(self):
        node1 = TextNode("link", TextType.BOLD, "http://example.com")
        node2 = TextNode("link", TextType.BOLD, "http://example.com")
        self.assertEqual(node1, node2)

    def test_noteq_url_diff(self):
        node1 = TextNode("link", TextType.BOLD, None)
        node2 = TextNode("link", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
