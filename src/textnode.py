from enum import Enum
from LeafNode import *

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"



class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return(
            isinstance(other, TextNode)
            and self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(tag = None, value = self.text)
            case TextType.BOLD:
                return LeafNode(tag = "b", value = self.text_type)
            case TextType.ITALIC:
                return f"<i>{self.text}</i>"
            case TextType.CODE:
                return f"<code>{self.text}</code>"
            case TextType.LINK:
                return
            case TextType.IMAGE:
                return





