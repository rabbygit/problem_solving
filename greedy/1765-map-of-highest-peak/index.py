import collections
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        res = [[-1] * cols for _ in range(rows)]
        q = collections.deque()

        # append all water cells to queue
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j]:
                    res[i][j] = 0
                    q.append((i, j))

        # run BFS
        while q:
            r, c = q.popleft()
            height = res[r][c]
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for nr, nc in neighbors:
                if (
                    nr >= 0
                    and nr < rows
                    and nc >= 0
                    and nc < cols
                    and res[nr][nc] == -1
                ):
                    res[nr][nc] = height + 1
                    q.append((nr, nc))

        return res
