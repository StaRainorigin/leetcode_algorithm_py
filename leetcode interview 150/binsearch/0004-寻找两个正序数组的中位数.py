from cmath import inf
from typing import List

# 1, 3, 5, 7, 9
# 0, 2, 4
# (3 + 4) / 2 = 3.5

# 1, 2, 4, 7, 9
# 0, 3, 5

# 1, 3, 5, 7
# 0, 2, 4
# 3

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n, m = len(nums1), len(nums2)
        nums1 = [-inf] + nums1 + [inf]
        nums2 = [-inf] + nums2 + [inf]
        
        left, right = 0, n + 1
        while left + 1 < right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            if nums1[i] <= nums2[j+1]:
                left = i
            else:
                right = i
        
        i = left
        j = (m + n + 1) // 2 - i
        max1 = max(nums1[i], nums2[j])
        min2 = min(nums1[i+1], nums2[j+1])
        return max1 if (m + n) % 2 else (max1 + min2) / 2
    
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     n, m = len(nums1), len(nums2)
    #     i, j = 0, 0
    #     nums = []
    #     while i < n and j < m:
    #         if nums1[i] < nums2[j]:
    #             nums.append(nums1[i])
    #             i += 1
    #         else:
    #             nums.append(nums2[j])
    #             j += 1
                
    #     while i < n:
    #         nums.append(nums1[i])
    #         i += 1
    #     while j < m:
    #         nums.append(nums2[j])
    #         j += 1
            
    #     mid = (0 + n + m) // 2
    #     return nums[mid] if (n + m) % 2 == 1 else (nums[mid-1]+nums[mid])/2
    
    
if __name__ == "__main__":
    nums1, nums2 = [1, 2], [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))