class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, canBuy):
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]
            
            if i == len(prices):
                return 0
            
            if canBuy: # if True
                memo[(i, canBuy)] = max(dfs(i+1, canBuy), dfs(i + 1, False) - prices[i])
            else:
                memo[(i, canBuy)] = max(dfs(i+1, canBuy), dfs(i+1, True) + prices[i])
            
            return memo[(i, canBuy)]
 
        return dfs(0, True)