import collections


class Solution:

    def minSteps(self, s: str, t: str) -> int:
        charMap, steps = collections.Counter(s), 0

        for c in t:
            if charMap[c] > 0:
                charMap[c] -= 1
            else:
                steps += 1

        return steps