class PrefixTree:

    def __init__(self):
        self.letters = [None]*26
        self.isWordEnd = False

    def insert(self, word: str) -> None:
        if not word:
            self.isWordEnd = True
            return
        
        char = ord(word[0])-ord('a')
        if not self.letters[char]:
            self.letters[char] = PrefixTree()
        
        self.letters[char].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.isWordEnd

        char = ord(word[0])-ord('a')

        if not self.letters[char]:
            return False

        return self.letters[char].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True

        char = ord(prefix[0])-ord('a')

        if not self.letters[char]:
            return False

        return self.letters[char].startsWith(prefix[1:])



        
        