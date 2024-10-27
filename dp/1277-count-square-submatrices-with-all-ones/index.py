import collections
from typing import List


class RecursiveSolution:
    # T.C and S.C: O(m * n)
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        result = 0

        def dfs(r: int, c: int):
            if r == ROWS or c == COLS or matrix[r][c] == 0:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]

            cache[(r, c)] = 1 + min(dfs(r + 1, c), dfs(r, c + 1), dfs(r + 1, c + 1))
            return cache[(r, c)]

        for r in range(ROWS):
            for c in range(COLS):
                result += dfs(r, c)

        return result


class DpSolution:
    # T.C and S.C: O(m * n)
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = collections.defaultdict(int)
        result = 0

        # top-to-bottom approach
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 1:
                    dp[(r, c)] = 1 + min(
                        dp[(r - 1, c)], dp[(r, c - 1)], dp[(r - 1, c - 1)]
                    )
                    result += dp[(r, c)]

        return result
