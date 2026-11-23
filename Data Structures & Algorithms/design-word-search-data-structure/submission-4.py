class WordDictionary:

    def __init__(self):
        self.letters = [None]*26
        self.isWordEnd = False


    def addWord(self, word: str) -> None:
        curr = self

        for char in word:
            index = ord(char)-ord('a')
            if not curr.letters[index]:
                curr.letters[index] = WordDictionary()
            curr = curr.letters[index]
        
        curr.isWordEnd = True

    def search(self, word: str) -> bool:

        if not word:
            return self.isWordEnd
        
        if word[0] == '.':
            for char in self.letters:
                if char and char.search(word[1:]):
                    return True
            return False
        else:
            char = ord(word[0]) - ord('a')

            if not self.letters[char]:
                return False

        
        return self.letters[char].search(word[1:])
