from typing import List

# 1 2 4 5 6 7 0, len = 7
# 7 0 1 2 4 5 6

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        k = 0
        
        # 寻找 k, 旋转数量
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                k = n - 1 - mid
                break
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        # 二分查找
        left, right = 0 - k, n - k
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else: 
                return (mid + n) % n
        
        return -1
        
        
        
if __name__ == "__main__":
    nums = [1, 2, 4, 5, 6, 7, 0]
    # nums = [7, 0, 1, 2, 4, 5, 6]
    print(Solution().search(nums, 0))
        