from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
    
        # ans = 0
        # for num in nums:
        #     ans ^= num
        # return ans

if __name__ == "__main__":
    print(Solution().singleNumber([4, 1, 2, 1, 2]))