import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_equal_nodes(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_equal_text(self):
        node1 = TextNode("Text A", TextType.TEXT)
        node2 = TextNode("Text B", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_not_equal_text_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_equal_with_none_url(self):
        node1 = TextNode("Example", TextType.TEXT, None)
        node2 = TextNode("Example", TextType.TEXT, None)
        self.assertEqual(node1, node2)

    def test_not_equal_url(self):
        node1 = TextNode("Link", TextType.LINK, "https://a.com")
        node2 = TextNode("Link", TextType.LINK, "https://b.com")
        self.assertNotEqual(node1, node2)

    def test_not_equal_to_non_textnode(self):
        node = TextNode("Hello", TextType.TEXT)
        self.assertNotEqual(node, "Hello")


if __name__ == "__main__":
    unittest.main()