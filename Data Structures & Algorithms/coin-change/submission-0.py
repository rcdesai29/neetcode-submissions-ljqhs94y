class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                change = a - c
                if change >= 0:
                    dp[a] = min(dp[a], 1 + dp[change])
        return dp[-1] if dp[-1] != amount + 1 else -1