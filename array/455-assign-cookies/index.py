import heapq
from typing import List


class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        result = gIdx = sIdx = 0
        gLength, sLength = len(g), len(s)

        while gIdx < gLength and sIdx < sLength:
            if g[gIdx] <= s[sIdx]:
                result += 1
                gIdx += 1
                sIdx += 1
            else:
                gIdx += 1

        return result

    def findContentChildren1(self, g: List[int], s: List[int]) -> int:
        result = 0
        heapq._heapify_max(g)
        heapq._heapify_max(s)

        while g and s:
            if s[0] >= g[0]:
                result += 1
                heapq._heappop_max(g)
                heapq._heappop_max(s)
            else:
                heapq._heappop_max(g)

        return result