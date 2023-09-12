from typing import List


class Solution:

    def leastBricks(self, wall: List[List[int]]) -> int:
        edgeMap = {}

        for row in range(len(wall)):
            edge = 0

            for col in range(len(wall[row]) - 1):
                edge += wall[row][col]
                edgeMap[edge] = edgeMap.get(edge, 0) + 1

        edgeCounts = edgeMap.values()

        return len(wall) - (max(edgeCounts) if edgeCounts else 0)