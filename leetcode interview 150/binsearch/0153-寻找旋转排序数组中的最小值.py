from typing import List

# 4, 5, 0, 1, 2 ,3
# 1, 2, 3, 4, 5, 0

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid + 1
        return nums[left]