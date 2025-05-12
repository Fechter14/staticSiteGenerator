import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        d = {"href": "www.google.com", "target": "_blank"}
        node = HTMLNode("p", "Test 1", props=d)
        self.assertEqual(node.props_to_html(), ' href="www.google.com" target="_blank"')

    def test_props_to_html2(self):
        d = {"href": "www.yahoo.com", "quality": "geriatric", "appearance": "cluttered"}
        node = HTMLNode("p", "Test 2", props=d)
        self.assertEqual(node.props_to_html(), ' href="www.yahoo.com" quality="geriatric" appearance="cluttered"')

    def tetest_props_to_html3(self):
        d = {"href": "www.msn.com"}
        node = HTMLNode(props=d)
        self.assertEqual(node.props_to_html(), ' href="www.msn.com"')

    def test_props_to_html4(self):
        node = HTMLNode("p", "Test 4")
        self.assertNotEqual(node.props_to_html(), ' href="www.google.com" target="_blank"')