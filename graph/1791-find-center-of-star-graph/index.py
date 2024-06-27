import collections
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodeMap = collections.defaultdict(int)
        n = len(edges)

        for i in range(n):
            src, dst = edges[i]
            nodeMap[src] += 1
            nodeMap[dst] += 1

            if i == n - 1:
                return src if nodeMap[src] == n else dst
