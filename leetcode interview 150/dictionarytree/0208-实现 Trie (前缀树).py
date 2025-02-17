class Node:

    __slots__ = 'son', 'end'
    def __init__(self):
        self.son = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = Node()

    def _find(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.son:
                return 0
            cur = cur.son[c]
        return 2 if cur.end else 1

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

    def search(self, word: str) -> bool:
        return self._find(word) == 2

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) != 0
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)




# class Trie:
#     def __init__(self):
#         self.words = set()
#         self.prefixs = set() 

#     def insert(self, word: str) -> None:
#         self.words.add(word)
#         prefix = ""
#         for c in word:
#             prefix += c
#             self.prefixs.add(prefix)

#     def search(self, word: str) -> bool:
#         return word in self.words

#     def startsWith(self, prefix: str) -> bool:
#         return prefix in self.prefixs


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)