class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        - Merging all overlapping intervals
        - No overlap = No Merge
        
        """
        intervals.sort(key=lambda pair:pair[0])
        res = [intervals[0]]
        print(intervals)
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][0] = min(res[-1][0], intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append([intervals[i][0], intervals[i][1]])

        
        return res