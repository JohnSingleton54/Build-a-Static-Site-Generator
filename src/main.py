from textnode import TextNode, TextType

def main():
    tn = TextNode(text="This is some anchor text", text_type=TextType.LINK_TEXTTYPE, url="https://www.boot.dev")
    print(tn.__repr__)

if __name__ == "__main__":
    main()
