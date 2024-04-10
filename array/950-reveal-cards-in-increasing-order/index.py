import collections
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0] * len(deck)
        q = collections.deque(range(len(deck)))

        for card in deck:
            idx = q.popleft()
            res[idx] = card

            if q:
                q.append(q.popleft())

        return res
