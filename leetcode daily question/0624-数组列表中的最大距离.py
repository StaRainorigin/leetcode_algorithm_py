from cmath import inf
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        mn, mx = inf, -inf
        for array in arrays:
            ans = max(ans, array[-1] - mn, mx - array[0])
            mn = min(mn, array[0])
            mx = max(mx, array[-1])
        return ans