class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                prevI, prevH = stack.pop()
                maxArea = max(maxArea, prevH * (i-prevI))
                start = prevI
            stack.append([start, h])
        
        n = len(heights)
        while stack:
            prevI, prevH = stack.pop()
            maxArea = max(maxArea, prevH * (n-prevI))
        return maxArea