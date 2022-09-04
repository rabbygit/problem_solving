from collections import Counter
from heapq import heappush, heappop

""" Complexity Analysis

Time Complexity: O(Nlogk) 

where N is the length of words. We count the frequency of each word in O(N) time,
then we add NN words to the heap, each in O(logk) time. 
Finally, we pop from the heap up to kk times or just sort all elements in the heap as the returned result, 
which takes O(k logk). As k≤N, O(N) + O(N logk ) + O(k logk ) = O(Nlogk)

Space Complexity: O(N), O(N) space is used to store our counter cnt while O(k) space is for the heap.
"""

class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        h = []

        for word, freq in cnt.items():
            heappush(h, Pair(word, freq))
            if len(h) > k:
                heappop(h)

        return [p.word for p in sorted(h, reverse=True)]