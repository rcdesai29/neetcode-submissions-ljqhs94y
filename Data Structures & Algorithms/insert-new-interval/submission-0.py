class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        #add all intervals that come before
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        #add merged
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+= 1
        res.append(newInterval)

        #add all remaining
        if i < n:
            res.extend(intervals[i:])
        return res

