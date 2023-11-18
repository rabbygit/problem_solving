from collections import Counter
from heapq import heappush, heappop

""" Complexity Analysis

Time Complexity: O(Nlogk) 

where N is the length of words. We count the frequency of each word in O(N) time,
then we add N words to the heap, each in O(logk) time. 
Finally, we pop from the heap up to k times 
and sort all elements in the heap to retun the result, 
which takes O(k logk). As k≤N, O(N) + O(N logk ) + O(k logk ) = O(Nlogk)

Space Complexity: O(N), O(N) space is used to store our counter cnt while O(k) space is for the heap.
"""

from collections import Counter
from heapq import heappush, heappop


class Pair:

    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    # determine whether the currently added element is smaller or not
    def __lt__(self, other):
        if self.freq < other.freq:
            return True
        elif self.freq > other.freq:
            return False
        # freq in ascending but lexically descending
        # so that, after sorting later we will get freq descending 
        # and lexically ascending
        return self.word > other.word


class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        minHeap = []

        for word, freq in cnt.items():
            heappush(minHeap, Pair(word, freq))
            # keep only top k freq words
            if len(minHeap) > k:
                heappop(minHeap)

        return [p.word for p in sorted(minHeap, reverse=True)]