class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles >= numExchange:
            full = numBottles // numExchange  # got exchanged
            left = numBottles % numExchange
            numBottles = full + left
            res += full

        return res
