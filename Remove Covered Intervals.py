class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: [x[0],-x[1]])
        previous_end, res = 0, 0
        for _, current_end in intervals:
            if current_end > previous_end:
                res+= 1
                previous_end = current_end
        return res
