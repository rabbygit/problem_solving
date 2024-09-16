from typing import List


class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        # convert HH:MM to minute
        for i, t in enumerate(timePoints):
            h, m = map(int, t.split(":"))
            timePoints[i] = h * 60 + m

        # sort the time point
        timePoints.sort()

        # distance of the final point to it's first clockwise point
        res = 24 * 60 - timePoints[-1] + timePoints[0]

        # calculate min diff of each timepoint clockwise
        for i in range(len(timePoints) - 1):
            diff = timePoints[i + 1] - timePoints[i]
            if diff == 0:
                return 0
            res = min(res, diff)

        return res
