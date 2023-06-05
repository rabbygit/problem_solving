from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        result = 0

        for p in prices:
            minPrice = min(minPrice, p)
            result = max(result, p - minPrice)

        return result