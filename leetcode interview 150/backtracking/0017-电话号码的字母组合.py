from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        maps = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        n = len(digits)
        ans = []

        def dfs(i: int, alphas: str):
            if i == n:
                ans.append(alphas)
                return
            for alpha in maps[digits[i]]:
                dfs(i + 1, alphas + alpha)

        dfs(0, "")
        return ans
