from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        ways = 0

        for x, y in self.pts:
            if (abs(px - x) != abs(py - y)) or x == px or y == py:
                continue
            ways += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]

        return ways
