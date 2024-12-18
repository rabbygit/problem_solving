from typing import List


class Solution:
    # T.C and S.C: O(n)
    # hint: https://www.youtube.com/watch?v=qlLHWd2j0ok&ab_channel=Techdose
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        res = prices.copy()
        stack.append(n - 1)

        for i in range(n - 2, -1, -1):
            while stack and prices[stack[-1]] > prices[i]:
                stack.pop()

            if stack:
                res[i] -= prices[stack[-1]]
            stack.append(i)

        return res
