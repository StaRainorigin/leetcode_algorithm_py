from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        # 由于 i 说明的是 i 之前的部分组成的单词, 所以如果包括到最后一个字符, 应该是 n + 1
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j: i] in words:
                    dp[i] = True
                    break
        
        return dp[-1]