from typing import List


# T.C: O(m * n) and S.C: O(k)
class Solution:

    def findFarmland(self, land: List[List[int]]) -> int:
        result = []
        m, n = len(land), len(land[0])
        bottomRight = []  # [i, j]

        def dfs(r, c):
            if r >= m or r < 0 or c >= n or c < 0 or land[r][c] == 0:
                return

            # farmland will be always rectangular
            bottomRight[0] = max(bottomRight[0], r)
            bottomRight[1] = max(bottomRight[1], c)

            land[r][c] = 0
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    bottomRight = [i, j]
                    dfs(i, j)
                    result.append([i, j, bottomRight[0], bottomRight[1]])

        return result
