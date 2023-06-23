from typing import List

from typing import List


class Solution:

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # there is an edge from a -> b
        edgesHash = {(a, b) for a, b in connections}
        neighbors = {city: [] for city in range(n)}
        visited = set()
        changes = 0

        # build the adjacency list
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal changes

            for ne in neighbors[city]:
                if ne in visited:
                    continue

                if (ne, city) not in edgesHash:
                    changes += 1

                visited.add(ne)
                dfs(ne)

        visited.add(0)
        dfs(0)

        return changes