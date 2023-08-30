from typing import List


class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        result = 0

        for i in range(n):
            result += piles[i * 2 + 1]

        return result