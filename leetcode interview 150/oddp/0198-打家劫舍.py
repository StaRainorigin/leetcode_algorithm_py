from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for num in nums:
            f0, f1 = f1, max(f1, f0 + num)
        return f1
    
    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n == 1:
    #         return nums[0]
    #     elif n == 2:
    #         return max(nums[0], nums[1])
    #     dp = [nums[0], max(nums[0], nums[1])]
    #     for i in range(2, n):
    #         dp.append(max(dp[i-1], nums[i] + dp[i-2]))
    #     return dp[-1]
    
    
if __name__ == "__main__":
    print(Solution().rob([2, 7, 9, 3, 1]))
    print(Solution().rob([1, 2, 3, 1]))
    
    
    # 2 7 11 11 12