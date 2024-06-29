import collections
from typing import List, Set


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.res = [[] for _ in range(n)]
        self.nodeMap = collections.defaultdict(list)

        for u, v in edges:
            self.nodeMap[u].append(v)

        for i in range(n):
            self.dfs(i, i, set())

        for i in range(n):
            self.res[i].sort()

        return self.res

    def dfs(
        self,
        curr: int,
        parent: int,
        visited: Set[int],
    ) -> List[List[int]]:
        visited.add(curr)
        for dst in self.nodeMap[curr]:
            if dst not in visited:
                self.res[dst].append(parent)
                self.dfs(dst, parent, visited)
