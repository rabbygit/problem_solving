import collections
from typing import List


class Solution:
    # T.C: O(n + nlogn)
    # S.C: O(n)
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        numsCount = collections.Counter(arr1)
        res = []

        for n in arr2:
            for _ in range(numsCount[n]):
                res.append(n)
            del numsCount[n]

        for n in sorted(numsCount.keys()):
            for _ in range(numsCount[n]):
                res.append(n)

        return res
