class Node:
    def __init__(self):
        """
        Purpo se: A trie node.
        """
        self.children = dict()
        self.is_word = False


class PrefixTree:
    def __init__(self):
        """
        Purpose: Prefix Tree root node.
        """
        self.root = Node()

    def insert(self, word):
        """
        Purpose: Insert a word into the tree.
        """
        root = self.root
        for char in word:
            if not root.children.get():
                root.children[char] = Node()
            root = root.children[char]
        root.end = True

    def search(self, word):
        """
        Purpose: Search a word in the tree.
        """
        root = self.root
        for char in word:
            if not root.children.get(char):
                return False
            root = root.children[char]
        return root.end

    def start_with(self, word):
        """
        Purpose: Search for a word that starts with a given word in the tree.
        """
        root = self.root
        for char in word:
            if not root.children.get(char):
                return False
            root = root.children[char]
        return True

    def print_tree(self):
        root = self.root
        level = 0
        while root:
            for child in root.children:
                print(child)
            print(f"{level}. Level")
            level += 1
            root = root.children.get(child)


if __name__ == "__main__":
    tree = PrefixTree()
    fruits = [
        "apples",
        "oranges",
        "bananas",
        "mangoes",
        "grapes",
        "strawberry",
        "avocado",
    ]

    [tree.insert(fruit) for fruit in fruits]

    print(tree.search("apples"))
    print(tree.start_with("or"))
    tree.print_tree()
