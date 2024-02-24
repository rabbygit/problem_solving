import collections
from typing import List


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        knownTo = set([0, firstPerson])
        timeMap = {}

        for p1, p2, t in meetings:
            if t not in timeMap:
                timeMap[t] = collections.defaultdict(list)
            timeMap[t][p1].append(p2)
            timeMap[t][p2].append(p1)

        def dfs(p: int, visited: set, adj: dict):
            if p in visited:
                return
            visited.add(p)
            knownTo.add(p)
            for nei in adj[p]:
                dfs(nei, visited, adj)

        for t in sorted(timeMap.keys()):
            visited = set()
            for p in timeMap[t]:
                if p in knownTo:
                    dfs(p, visited, timeMap[t])

        return list(knownTo)
