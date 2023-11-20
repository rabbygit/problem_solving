class Solution:

    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        # negative number like -5 in the target cell, 6 health point needed to survive 
        # and for non-negative number in this cell, need 1 hp to survive.
        dp[m - 1][n], dp[m][n - 1] = 1, 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]

                if dp[i][j] <= 0:
                    # it means health point reminds after spent
                    # like go from +5 to +1, 1-5 = -4, need just 1 point
                    dp[i][j] = 1

        return dp[0][0]