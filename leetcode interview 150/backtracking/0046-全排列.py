from typing import List

class TreeNode:
    def __init__(self):
        self.val = 0
        self.sons = []

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = set()
        cur = []
        ans = []
        
        def backtracking():
            if len(cur) == n:
                ans.append(cur[:])
            
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    cur.append(num)
                    backtracking()
                    visited.remove(num)
                    cur.pop()
            
        backtracking()
        return ans