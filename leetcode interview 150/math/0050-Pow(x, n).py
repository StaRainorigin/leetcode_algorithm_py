from bisect import bisect_left


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        m = abs(n)
        while m:
            if m & 1:
                ans *= x
            x *= x
            m >>= 1
        return ans if n >= 0 else 1/ans
        
        
        
        
        # m = abs(n)
        # dp = [(1, x)]
        # i, j = 2, 1
        # while i < m:
        #     dp.append((i, dp[j-1][1]*dp[j-1][1]))
        #     i *= 2
        #     j += 1
        
        # ans = 1
        # while m > 0:
        #     for index in range(len(dp)-1, -1, -1):
        #         if m >= dp[index][0]:
        #             ans *= dp[index][1]
        #             m -= dp[index][0]
        #             break
        # return ans if n >= 0 else 1 / ans
        
        
        
        # ans = 1
        # for _ in range(abs(n)):
        #     ans *= x
        # return ans if n >= 0 else 1/ans
        
        
if __name__ == "__main__":
    print(Solution().myPow(2, 10))
    # arr = [(1, 2), (2, 4), (4, 16), (8, 256)]
    # print(bisect_left(arr, 3, key=lambda x: x[0]))