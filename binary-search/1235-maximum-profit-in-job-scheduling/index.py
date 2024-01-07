import bisect
from typing import List


class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int],
                      profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            elif i in cache:
                return cache[i]

            # we have two choices, include the current interval or not
            res = dfs(i + 1)  # not include

            # include
            # find first job that has greater or equal starting time 
            # than the current job's endtime
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return cache[i]

        return dfs(0)