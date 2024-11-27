import collections
from typing import List


class Solution:
    # T.C: q * (n+q) and S.C: O(n+q)
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        adj = [[i + 1] for i in range(n)]
        print(adj)

        def shortest_path():
            visited = set()
            q = collections.deque()
            q.append((0, 0))
            visited.add(0)

            while q:
                node, path_length = q.popleft()
                if node == n - 1:
                    return path_length
                for nei in adj[node]:
                    if nei not in visited:
                        q.append((nei, path_length + 1))
                        visited.add(nei)

        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(shortest_path())

        return res
