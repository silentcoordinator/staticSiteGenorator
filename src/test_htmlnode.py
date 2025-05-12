import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single_prop(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com"})
        output = node.props_to_html()
        self.assertEqual(output, ' href="https://example.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(tag="img", props={"src": "image.png", "alt": "An image"})
        output = node.props_to_html()
        self.assertIn('src="image.png"', output)
        self.assertIn('alt="An image"', output)
        self.assertTrue(output.startswith(" "))
        self.assertEqual(output.count("="), 2)

    def test_props_to_html_empty_props(self):
        node = HTMLNode(tag="div", props={})
        output = node.props_to_html()
        self.assertEqual(output, "")

if __name__ == "__main__":
    unittest.main()
