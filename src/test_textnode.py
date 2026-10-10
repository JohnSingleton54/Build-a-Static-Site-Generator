import unittest
from textnode import TextNode, TextType




class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXTTYPE)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXTTYPE)
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXTTYPE)
        node2 = TextNode("C4 ENERGY YOU CAN FEEL", TextType.BOLD_TEXTTYPE)
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXTTYPE)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXTTYPE)
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
