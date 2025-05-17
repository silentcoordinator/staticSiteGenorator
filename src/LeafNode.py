from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self,tag,value):
        super().__init__(tag,value, children = None, props = None)

    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.tag is None:
            return print(f"{self.value}")
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"




