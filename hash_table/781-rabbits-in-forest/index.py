import collections
from typing import List


class Solution:
    # T.C and S.C: O(n)
    def numRabbits(self, answers: List[int]) -> int:
        rabbitsMap = collections.defaultdict(int)
        count = 0

        for rabbitGroup in answers:
            if rabbitGroup == 0:
                count += 1
                continue

            rabbitsMap[rabbitGroup] += 1
            if rabbitGroup + 1 == rabbitsMap[rabbitGroup]:
                rabbitsMap[rabbitGroup] = 0
                count = count + rabbitGroup + 1

        for k, v in rabbitsMap.items():
            if v > 0:
                count = count + k + 1

        return count
