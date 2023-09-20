class Solution:

    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int,
                        targetCapacity: int) -> bool:
        visited = set()

        def dfs(total):
            if total == targetCapacity:
                return True

            if total < 0 or total > jug1Capacity + jug2Capacity or total in visited:
                return False

            visited.add(total)

            return (dfs(total + jug1Capacity) or dfs(total - jug1Capacity)
                    or dfs(total + jug2Capacity) or dfs(total - jug2Capacity))

        return dfs(0)