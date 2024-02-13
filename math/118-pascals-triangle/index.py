from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for r in range(1, numRows):
            sub = [1] * (r + 1)

            for c in range(1, r):
                sub[c] = res[r - 1][c - 1] + res[r - 1][c]

            res.append(sub.copy())

        return res
