from typing import List


class Solution:

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        lastValidIdx, result = 0, 1

        for idx in range(1, len(pairs)):
            a, b = pairs[lastValidIdx]
            c, d = pairs[idx]

            if d < b:
                # found a small upper bound
                lastValidIdx = idx
            elif b < c:
                lastValidIdx = idx
                result += 1

        return result