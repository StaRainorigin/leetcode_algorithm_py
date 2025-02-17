class TrieNode:
    __slots__ = 'son', 'end'  
    def __init__(self):
        self.son = {}  # 子节点
        self.end = False  # 是否是一个单词的结尾

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # 根节点

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = TrieNode()  # 如果字符不存在，创建新节点
            cur = cur.son[c]  # 移动到子节点
        cur.end = True  # 标记单词结尾

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.end  # 如果到达单词末尾，返回是否是单词结尾
            c = word[index]
            if c != '.':
                if c not in node.son:
                    return False  # 如果字符不匹配，返回 False
                return dfs(node.son[c], index + 1)  # 递归检查下一个字符
            else:
                # 如果是通配符 '.'，尝试所有可能的子节点
                for key in node.son:
                    if dfs(node.son[key], index + 1):
                        return True
                return False

        return dfs(self.root, 0)  # 从根节点开始搜索
    

if __name__ == "__main__":
    obj = WordDictionary()
    print(obj.addWord("a"))
    print(obj.addWord("a"))
    print(obj.search("."))
    print(obj.search("a"))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)