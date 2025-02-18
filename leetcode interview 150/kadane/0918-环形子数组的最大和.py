from cmath import inf
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max, ans_max = -inf, -inf
        cur_min, ans_min = inf, inf
        sum = 0
        for num in nums:
            sum += num
            cur_max = max(num, cur_max + num)
            cur_min = min(num, cur_min + num)
            ans_max = max(cur_max, ans_max)
            ans_min = min(cur_min, ans_min)
        return ans_max if sum == ans_min or ans_max > sum - ans_min else sum - ans_min
        