class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans
    

if __name__ == "__main__":
    print(Solution().trailingZeroes(20))