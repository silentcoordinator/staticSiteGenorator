from textnode import TextNode
def main():
    newNode = TextNode("this is some anchor text", "link", "https://boot.dev")
    print(newNode)
    print(newNode.text)
    print(newNode.text_type)
    print(newNode.url)
    x = repr(newNode)
    print(x)
main()