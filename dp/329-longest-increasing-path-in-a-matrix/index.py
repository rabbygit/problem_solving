class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def dfs(r, c, prevValue):
            if r < 0 or c < 0 or r >= rows or c >= cols or prevValue >= matrix[
                    r][c]:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]

            # run dfs on 4 possible directions
            # and cache the max lip value for this current position
            lip = max(1, 1 + dfs(r + 1, c, matrix[r][c]),
                      1 + dfs(r - 1, c, matrix[r][c]),
                      1 + dfs(r, c + 1, matrix[r][c]),
                      1 + dfs(r, c - 1, matrix[r][c]))

            cache[(r, c)] = lip
            return lip

        # calculate lip for every position
        result = 0
        for r in range(rows):
            for c in range(cols):
                result = max(result, dfs(r, c, -1))

        return result
