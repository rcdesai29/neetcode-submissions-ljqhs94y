class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        gas = gas + gas
        cost = cost + cost

    
        l = 0
        tank = 0
        starting = -1
        for r in range(len(gas)):
            tank = tank + gas[r] - cost[r] 
            while tank < 0:
                tank -=  gas[l] - cost[l]
                l += 1
            if tank >= 0 and (r - l) + 1 == n:
                starting = l
        return starting
