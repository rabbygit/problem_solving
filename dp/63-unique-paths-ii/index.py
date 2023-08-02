class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = '#'

        obstacleGrid[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if obstacleGrid[i][j] == '#': continue

                down = 0
                right = 0
                if i < m - 1 and obstacleGrid[i + 1][j] != '#':
                    down = obstacleGrid[i + 1][j]
                if j < n - 1 and obstacleGrid[i][j + 1] != '#':
                    right = obstacleGrid[i][j + 1]

                obstacleGrid[i][j] = obstacleGrid[i][j] + down + right

        return obstacleGrid[0][0]