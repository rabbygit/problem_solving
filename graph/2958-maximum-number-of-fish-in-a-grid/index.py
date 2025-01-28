from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            fish = grid[r][c]
            grid[r][c] = 0 # marked as visited
            return fish + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))

        return res
