from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i, j, n, m = 0, 0, len(nums1), len(nums2)
        ans = []
        while i < n and j < m and k > 0:
            ans.append([nums1[i]])