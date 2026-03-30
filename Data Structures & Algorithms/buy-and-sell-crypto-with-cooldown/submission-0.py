class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}

        def dfs(i, buy):
            if (i, buy) in dp:
                return dp[(i,buy)]
            
            if i >= len(prices):
                return 0

            cooldown = dfs(i + 1, buy)
            if buy:
                buying = dfs(i+1, not buy) - prices[i]
                dp[(i, buy)] = max(cooldown, buying)
            else:
                sell = dfs(i + 2, not buy) + prices[i]
                dp[(i, buy)] = max(cooldown, sell)
            return dp[(i, buy)]
        return dfs(0, True)
            

