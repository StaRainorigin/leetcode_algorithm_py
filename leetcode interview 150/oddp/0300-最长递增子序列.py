from bisect import bisect_left, bisect_right
from typing import List

# 1, 1, 1, 2, 2, 3, 4, 4

class Solution:
    # 贪心 + 二分搜索
    def lengthOfLIS(self, nums: List[int]) -> int:
    # 由于之前说过，顺序数组, 顺序性质的查找都可以用二分法替代
    
    # 改算法是维持
        dp = []
        for num in nums:
            i = bisect_left(dp, num) # 在已知递增子序列中, 找能插入的位置
            if i == len(dp):    # 最后面说明比所有元素都大,
                dp.append(num)  #   放最后面
            else:               # 能找到则替换
                dp[i] = num     #   替换后可能列表中的序列并不是所求序列
        return len(dp)          #   但我们要的是最大长度, 最大长度是不会因为这个受影响的
                                #   如果后面替换着替换着长度变长了, 说明之前的列表的元素已经全被替换掉了

    
    # 动态规划
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [0]
    #     for i in range(n):
    #         count = 1
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 count = max(dp[j + 1] + 1, count)
    #         dp.append(count)
    #     return max(dp)
    
if __name__ == "__main__":
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 1, 101, 18]))