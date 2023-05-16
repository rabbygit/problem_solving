import heapq


class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        cardCount = {}
        for n in hand:
            cardCount[n] = 1 + cardCount.get(n, 0)

        minHeap = list(cardCount.keys())
        heapq.heapify(minHeap)

        while minHeap:
            firstElement = minHeap[0]

            for i in range(firstElement, firstElement + groupSize):
                if i not in cardCount:
                    return False
                cardCount[i] -= 1
                if cardCount[i] == 0:
                    if minHeap[0] != i:
                        return False
                    heapq.heappop(minHeap)

        return True
