import collections
import heapq


class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        cardCount = collections.Counter(hand)
        minHeap = list(cardCount.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for card in range(first, first + groupSize):
                if card not in cardCount:
                    return False

                cardCount[card] -= 1
                if cardCount[card] == 0:
                    if card != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
                    del cardCount[card]

        return True
