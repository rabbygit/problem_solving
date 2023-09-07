from typing import List


# ref: https://leetcode.com/problems/minimum-time-difference/solutions/474787/python3-o-nlogn-time-with-detailed-explanation/
class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        res = float('inf')

        for i in range(len(timePoints)):
            timePoints[i] = self.convertToMin(timePoints[i])

        # sort the time point
        timePoints.sort()

        # calculate min diff of each timepoint clockwise
        for i in range(len(timePoints) - 1):
            res = min(res, timePoints[i + 1] - timePoints[i])

        # distance of the final point to it's first clockwise point
        res = min(res, 60 * 24 - timePoints[-1] + timePoints[0])

        return res

    def convertToMin(self, time: str):
        h, m = time.split(':')
        return int(h) * 60 + int(m)
