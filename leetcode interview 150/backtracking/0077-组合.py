from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return list(combinations(range(1, n+1), k)
        
        if not n or not k:
            return []
        ans = []
        
        def backtracking(cur: int, nums: list):
            if len(nums) == k:
                ans.append(nums[:])
            
            if n - cur + 1 < k - len(nums):
                return
            
            for i in range(cur, n+1):
                nums.append(i)
                backtracking(i+1, nums)
                nums.pop()
        
        backtracking(1, [])
        
        return ans
    
if __name__ == "__main__":
    print(Solution().combine(4, 2))