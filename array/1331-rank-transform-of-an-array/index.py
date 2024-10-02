from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        numsMap = {}

        for idx, n in enumerate(sorted(set(arr))):
            numsMap[n] = idx + 1

        for idx, n in enumerate(arr):
            arr[idx] = numsMap[n]

        return arr
