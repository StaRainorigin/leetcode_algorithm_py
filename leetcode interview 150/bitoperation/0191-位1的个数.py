class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans += 1 if n & 1 == 1 else 0
            n >>= 1
        return ans
            