import collections
from typing import List


class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        N = len(grid)
        res, visited, q = 1, set(), collections.deque()
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),
                      (1, 0), (1, 1)]

        q.append((0, 0))
        visited.add((0, 0))

        while q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()

                if r == N - 1 and c == N - 1:
                    return res

                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if -1 < row < N and -1 < col < N and grid[row][
                            col] == 0 and (row, col) not in visited:
                        q.append((row, col))
                        visited.add((row, col))

            res += 1

        return -1
