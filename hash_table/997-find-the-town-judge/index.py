import collections
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedBy = collections.defaultdict(int)
        trustCount = collections.defaultdict(int)

        for person1, person2 in trust:
            trustedBy[person2] += 1
            trustCount[person1] += 1

        for person in range(1, n + 1):
            if trustedBy[person] == n - 1 and trustCount[person] == 0:
                return person

        return -1
