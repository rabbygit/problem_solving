import collections
from typing import List


class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        visited, result, start = set(), [], None

        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)

        for k, v in adj.items():
            if len(v) == 1:
                start = k
                break

        def dfs(key):
            if key in visited:
                return

            visited.add(key)
            result.append(key)

            for k in adj[key]:
                dfs(k)

        dfs(start)

        return result
