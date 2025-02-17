import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag= "<p>", value = "This is an HTML node")
        print(node)
        pass

if __name__ == "__main__":
    unittest.main()