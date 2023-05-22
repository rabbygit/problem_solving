from typing import List


class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        prevEnd = intervals[0][1]
        remove = 0

        for j in range(1, len(intervals)):
            if intervals[j][0] < prevEnd:
                remove += 1
                prevEnd = min(intervals[j][1], prevEnd)
            else:
                prevEnd = intervals[j][1]

        return remove
