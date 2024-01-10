from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


class Solution1:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i >= len(cost):
                return 0
            elif i in cache:
                return cache[i]

            cache[i] = min(cost[i] + dfs(i + 1), cost[i] + dfs(i + 2))
            return cache[i]

        dfs(0)
        return min(cache[0], cache[1])