from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        max_moves = 0

        for col in range(n - 1, -1, -1):
            for row in range(m - 1, -1, -1):
                if row > 0 and col + 1 < n and grid[row][col] < grid[row - 1][col + 1]:
                    dp[row][col] = max(dp[row][col], dp[row - 1][col + 1] + 1)
                if col + 1 < n and grid[row][col] < grid[row][col + 1]:
                    dp[row][col] = max(dp[row][col], dp[row][col + 1] + 1)
                if (
                    row + 1 < m
                    and col + 1 < n
                    and grid[row][col] < grid[row + 1][col + 1]
                ):
                    dp[row][col] = max(dp[row][col], dp[row + 1][col + 1] + 1)

                if col == 0:
                    max_moves = max(max_moves, dp[row][0])

        return max_moves
