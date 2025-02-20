from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        for i in range(1,amount + 1):
            min_coins = amount + 1
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] >= 0:
                    min_coins = min(min_coins, dp[i - coin] + 1)
            dp.append(min_coins if min_coins < amount + 1 else -1)
                
        return dp[amount]
    
    
if __name__ == "__main__":
    print(Solution().coinChange([1, 2, 5], 11))