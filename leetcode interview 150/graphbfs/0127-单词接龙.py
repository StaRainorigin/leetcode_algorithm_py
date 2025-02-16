from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = {beginWord} if beginWord in wordList else set()
        q = deque([beginWord])
        count = 1
        
        def check(word1: str, word2: str):
            n, m = len(word1), len(word2)
            if n != m: return False
            flag = False
            for i in range(n):
                if word1[i] != word2[i]:
                    if flag:
                        return False
                    else:
                        flag = True
            return flag
        
        while q:
            count += 1
            nxt = []
            while q:
                cur = q.popleft()
                for word in wordList:
                    if word not in visited and check(cur, word):
                        if word == endWord:
                            return count
                        else:
                            visited.add(word)
                            nxt.append(word)
            q.extend(nxt)

        return 0
    
if __name__ == "__main__":
    beginWord, endWord = "hit", "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))