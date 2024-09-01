from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        idx = 0
        res = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = original[idx]
                idx += 1

        return res
