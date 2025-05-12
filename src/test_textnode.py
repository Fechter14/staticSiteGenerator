import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        #examples below use asserts to break down each element of the test
        self.assertNotEqual("wwww.google.com", node.url)
        self.assertEqual(None, node.url)
        self.assertEqual(None, node2.url)
        self.assertEqual(TextType.BOLD, node.text_type)
        self.assertEqual(TextType.BOLD, node2.text_type)
        self.assertEqual("This is a text node", node.text)
        self.assertEqual("This is a text node", node2.text)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is  a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_type_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_no_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_two_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.yahoo.com")
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, bold, www.google.com)")

if __name__ == "__main__":
    unittest.main()