from htmlnode import *
from LeafNode import LeafNode
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(value = None, tag = tag, children = children, props = props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag was in node")

        if self.children is None:
            raise ValueError("children cannot be None")

        inner_html =""

        for child in self.children:
            inner_html += child.to_html()


        return f"<{self.tag}>{inner_html}</{self.tag}>"
