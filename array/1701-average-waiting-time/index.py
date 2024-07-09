from typing import List


class Solution:
    # T.C: O(n) and S.C: O(1)
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        orderPrepared = customers[0][0]
        totalWaitingTime = 0

        for arrival, time in customers:
            if orderPrepared < arrival:
                orderPrepared = arrival

            orderPrepared += time
            totalWaitingTime += orderPrepared - arrival

        return totalWaitingTime / len(customers)
