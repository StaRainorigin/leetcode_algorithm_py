from bisect import bisect_left
from typing import List

# 1 2 3 3 3 3 8 8 8 8 9

class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
        
    #     def bin_search(nums: List[int], target: int) -> int:
    #         left, right = 0, len(nums)
    #         while left < right:
    #             mid = (left + right) // 2
    #             if nums[mid] < target:
    #                 left = mid + 1
    #             else:
    #                 right = mid
    #         return left
    
    #     start = bin_search(nums, target)
    #     if start == len(nums) or nums[start] != target:
    #         return [-1, -1]
    #     end = bin_search(nums, target+1) - 1
    #     return [start, end]
            
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect_left(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = bisect_left(nums, target + 1) - 1
        return [start, end]
    
            
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     n = len(nums)
    #     left, right = 0, n
    #     left_border, right_border = -1, -1
    #     while left < right:
    #         mid = (left + right) // 2
    #         if nums[mid] == target and ((mid == 0) or (mid > 0 and nums[mid-1] != target)):
    #             left_border = mid
    #             break
    #         if nums[mid] < target:
    #             left = mid + 1
    #         else:
    #             right = mid
                
    #     if left_border >= 0:
    #         left, right = left_border, n
    #         while left < right:
    #             mid = (left + right) // 2
    #             if nums[mid] == target and (mid == n-1 or (mid < n-1 and nums[mid+1] != target)):
    #                 right_border = mid
    #             if nums[mid] > target:
    #                 right = mid
    #             else:
    #                 left = mid + 1
                    
    #     return [left_border, right_border]
    
if __name__ == "__main__":
    # nums = [1, 2, 3, 3, 3, 3, 3, 8, 8, 8, 9]
    nums = []
    print(Solution().searchRange(nums, 0)) 