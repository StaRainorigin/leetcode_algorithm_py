from cmath import inf
from typing import List


class Solution:
    # 动态规划(优化)
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        cur = -inf
        for num in nums:
            cur = max(cur, 0) + num
            ans = max(cur, ans)
        return ans
            
    # 动态规划(基础)
    # def maxSubArray(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [0] * n
    #     dp[0] = nums[0]
    #     for i in range(1, n):
    #         dp[i] = max(dp[i-1], 0) + nums[i]
    #     return max(dp)
    
    
    # kadane 实现
    # def maxSubArray(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
        
    #     ans = -inf
    #     cur = -inf
    #     for num in nums:
    #         cur = max(num, cur + num)
    #         ans = max(cur, ans)
    #     return ans