from testnode import TextNode, TextType

def main():
    dummy = TextNode("this is some text", TextType.LINK, "https://www.bootdev.com")
    #dummy.__repr__()
    print(dummy)

main()