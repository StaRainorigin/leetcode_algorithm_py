from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        nums = defaultdict(list)
        for i, num in enumerate(arr):
            nums[num].append(i)
        self.nums = nums

    def query(self, left: int, right: int, value: int) -> int:
        indexs = self.nums[value]
        return bisect_right(indexs, right) - bisect_left(indexs, left)

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)