import collections
from typing import List


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        adjacency = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq[0], eq[1]
            adjacency[a].append([b, values[i]])
            adjacency[b].append([a, 1 / values[i]])

        def bfs(src, des):
            if src not in adjacency or des not in adjacency:
                return -1

            q, visited = collections.deque(), set()
            q.append([src, 1])
            visited.add(src)

            while q:
                n, w = q.popleft()

                if n == des:
                    return w

                for nei, weight in adjacency[n]:
                    if nei not in visited:
                        q.append([nei, w * weight])
                        visited.add(nei)

            return -1

        return [bfs(q[0], q[1]) for q in queries]
