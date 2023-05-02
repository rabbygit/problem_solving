class Solution:
    #[ 1, 2, 3
    #  4, 5, 6 ]
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]
        grid[m - 1][n - 1] = 1  # base case

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                down = 0
                right = 0

                # if the position is in bound then set the proper value
                if i < m - 1:
                    down = grid[i + 1][j]
                if j < n - 1:
                    right = grid[i][j + 1]

                # calculate from bottom-to-up
                grid[i][j] = grid[i][j] + down + right

        return grid[0][0]