from typing import List


class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        timeMap = {}
        res = 0

        for t in time:
            rem = t % 60

            if rem == 0:
                res += timeMap.get(rem, 0)
            else:
                res += timeMap.get(60 - rem, 0)

            timeMap[rem] = timeMap.get(rem, 0) + 1

        return res