import sys
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # using Bellman-Ford Algorithm
        INF = sys.maxsize
        previous = [INF] * n  # keep shortest path using at most (k-1)th edges
        current = [INF] * n  # keep shortest path using at most k th edges

        previous[src] = 0

        for k in range(1, k+2):
            current[src] = 0

            for flight in flights:
                previous_flight, current_flight, cost = flight

                # path relaxation for every edge if needed
                if previous[previous_flight] + cost < current[current_flight]:
                    current[current_flight] = previous[previous_flight] + cost

            # after every iteration update the previous state
            previous = current.copy()

        if current[dst] == INF:
            return -1
        return current[dst]
