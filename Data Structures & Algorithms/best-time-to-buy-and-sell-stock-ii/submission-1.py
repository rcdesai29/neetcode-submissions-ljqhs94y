class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, canBuy):
            if i == len(prices):
                return 0
            
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            
            res = dfs(i + 1, canBuy)

            if canBuy:
                bought = dfs(i+1, False) - prices[i]
                res = max(res, bought)
            else:
                sold = dfs(i+1, True) + prices[i]
                res = max(res, sold)
            
            dp[(i, canBuy)] = res
            return res
        return dfs(0, True)