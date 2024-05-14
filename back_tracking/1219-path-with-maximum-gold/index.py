from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            res = tmp = grid[r][c]
            grid[r][c] = 0

            res = max(
                res,
                res + dfs(r + 1, c),
                res + dfs(r - 1, c),
                res + dfs(r, c + 1),
                res + dfs(r, c - 1),
            )

            grid[r][c] = tmp
            return res

        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))

        return res
