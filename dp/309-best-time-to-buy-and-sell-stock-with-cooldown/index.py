class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        profitHash = {}  # (index, can_buy) -> profit up to this point

        def dfs(index, can_buy):
            # base-case
            if index >= len(prices):
                return 0

            # profit already calculated
            if (index, can_buy) in profitHash:
                return profitHash[(index, can_buy)]

            # cooldown choice
            cooldown = dfs(index + 1, can_buy)

            # buying is allowed
            if can_buy:
                # profit after buying
                after_buy = dfs(index + 1, False) - prices[index]
                profitHash[(index, can_buy)] = max(after_buy, cooldown)
            else:
                # selling is allowed
                # profit after selling
                after_sell = dfs(index + 2, True) + prices[index]
                profitHash[(index, can_buy)] = max(after_sell, cooldown)

            return profitHash[(index, can_buy)]

        return dfs(0, True)
