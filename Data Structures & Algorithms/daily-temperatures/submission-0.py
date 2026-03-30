class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * (len(temperatures))
        stack = []
        #append
        #pop
        #push

        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures), 1):
                if temperatures[j] > temperatures[i]:
                    res[i] += (j-i)
                    break
        return res