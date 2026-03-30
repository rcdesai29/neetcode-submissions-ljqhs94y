class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p,s in pairs:
            time = (target - p)/s
            stack.append(time)
            while len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
            
