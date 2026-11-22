class PrefixNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = PrefixNode()
            curr = curr.children[index]
        curr.isLeaf = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isLeaf

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True