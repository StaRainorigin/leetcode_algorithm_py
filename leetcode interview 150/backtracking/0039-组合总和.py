from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        n = len(candidates)
        nums = []
        ans = []
        
        def backtracking(sum: int, i: int):
            if sum > target:
                return
            elif sum == target:
                ans.append(nums[:])
                
            for j in range(i, n):
                candidate = candidates[j]
                nums.append(candidate)
                backtracking(sum + candidate, j)
                nums.remove(candidate)
                
        backtracking(0, 0)
        return ans