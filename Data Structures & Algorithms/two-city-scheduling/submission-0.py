class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        costs.sort(key=lambda x:(x[0] - x[1]))

        res = 0

        for i in range(n):
            res += costs[i][0]
        
        for i in range(n, len(costs)):
            res += costs[i][1]
            
        return res