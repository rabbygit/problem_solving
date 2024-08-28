from typing import List


class Solution:
    # T.C and S.C: O(m * n)
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visited, count = set(), 0

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or grid2[r][c] == 0
                or (r, c) in visited
            ):
                # end of the island, return True
                return True

            res = True
            if grid1[r][c] == 0:
                # cell is missing in grid1, return False
                res = False

            visited.add((r, c))
            # recursively visit in 4 directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                res = dfs(r + dr, c + dc) and res

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r, c) not in visited and dfs(r, c):
                    count += 1

        return count
