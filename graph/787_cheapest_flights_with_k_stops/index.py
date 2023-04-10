from typing import List


class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, k: int) -> int:
        # using Bellman-Ford Algorithm
        INF = float("inf")
        prices = [INF] * n  # keep shortest path using at most (k-1)th edges
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices.copy()

            for flight in flights:
                s, d, cost = flight

                if prices[s] == INF:
                    continue

                # path relaxation for every edge if needed
                if prices[s] + cost < tempPrices[d]:
                    tempPrices[d] = prices[s] + cost

            # after every iteration update the previous state
            prices = tempPrices

        return -1 if prices[dst] == INF else prices[dst]
