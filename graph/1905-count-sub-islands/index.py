from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visited = set()

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or grid2[r][c] == 0
                or (r, c) in visited
            ):
                return True

            res = True
            if grid1[r][c] == 0:
                res = False

            visited.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                res = dfs(r + dr, c + dc) and res

            return res

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r, c) not in visited and dfs(r, c):
                    count += 1

        return count
