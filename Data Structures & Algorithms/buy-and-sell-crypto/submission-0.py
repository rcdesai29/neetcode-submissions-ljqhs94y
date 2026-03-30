class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l 
        maxp = 0
        while r+1 < len(prices):
            
            if prices[l] >= prices[r]:
                l = r
                r+=1
            else:
                r+=1
            maxp = max(prices[r] - prices[l], maxp)
        return maxp
            