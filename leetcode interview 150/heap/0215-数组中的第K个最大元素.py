import random
from typing import List
from heapq import heapify, heappop, heappush, heappushpop


sorted()

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        big, equal, small = [], [], []
        for num in nums:
            if num > pivot:
                big.append(num)
            elif num < pivot:
                small.append(num)
            else:
                equal.append(num)
        if k <= len(big):
            return self.findKthLargest(big, k)
        if len(nums) - len(small) < k:
            return self.findKthLargest(small, k - len(nums) + len(small))
        return pivot
        
        
        
        
        # n = len(nums)
        # if n < k:
        #     return
        # i = 0
        # heap = []
        # heapify(heap)
        # while i < n:
        #     if i < k:
        #         heappush(heap, nums[i])
        #     else:
        #         heappushpop(heap, nums[i])
        #     i += 1
        # return heappop(heap)
        
        