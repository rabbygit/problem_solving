import collections
from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r < rows and r >= 0 and c < cols and c >= 0 and grid[r][
                            c] == '1' and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    total += 1

        return total

    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        visited = set()
        totalIslands = 0
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r >= m or r < 0 or c >= n or c < 0 or grid[r][c] == '0' or (
                    r, c) in visited:
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    totalIslands += 1

        return totalIslands