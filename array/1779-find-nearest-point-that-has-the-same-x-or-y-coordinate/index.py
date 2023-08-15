class Solution:

    def nearestValidPoint(self, x: int, y: int,
                          points: List[List[int]]) -> int:

        index, smallest = -1, float("inf")

        for i, (r, c) in enumerate(points):
            if x == r or y == c:
                dx, dy = x - r, y - c
                if abs(dx + dy) < smallest:
                    smallest = abs(dx + dy)
                    index = i

        return index