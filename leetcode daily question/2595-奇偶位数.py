from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        is_odd = True
        odd = 0
        even = 0
        while n > 0:
            if is_odd:
                odd += 1 if n & 1 == 1 else 0
            else:
                even += 1 if n & 1 == 1 else 0
            is_odd = not is_odd
            n = n // 2
        return [odd, even]