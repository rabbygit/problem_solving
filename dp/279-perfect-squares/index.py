import math


class Solution:

    def numSquares(self, n: int) -> int:
        maxSquare = int(math.sqrt(n))
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, maxSquare + 1):
                square = s * s
                if target - square >= 0:
                    dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]


class Solution1:

    def numSquares(self, n: int) -> int:
        maxSquare = int(math.sqrt(n))
        cache = {}
        cache[0] = 0

        def dfs(target):
            if target in cache:
                return cache[target]
            
            res = n
            for s in range(1, maxSquare + 1):
                sq = s * s
                if target - sq >= 0:
                    res = min(res, 1 + dfs(target - sq))

            cache[target] = res
            return cache[target]

        return dfs(n)