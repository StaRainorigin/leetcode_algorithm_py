from functools import reduce
from typing import List

# (0, 0) -> (0, 1) -> (1, 0)

class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            b = (b ^ num) & ~a
            a = (a ^ num) & ~b
        return b
    
    
if __name__ == "__main__":
    print(Solution().singleNumber([2, 5, 5, 3, 3, 3, 5, 1, 1, 1]))