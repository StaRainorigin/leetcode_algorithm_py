from functools import reduce


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        m = (left ^ right).bit_length()
        return left & ~((1 << m)-1)
    
if __name__ == "__main__":
    print(Solution().rangeBitwiseAnd(0, 1))