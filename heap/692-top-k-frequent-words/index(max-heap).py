import heapq

""" Complexity Analysis

Let NN be the length of words.

Time Complexity: O(N+klogN)

We count the frequency of each word in O(N) time and then heapify the list of unique words in O(N) time.
Each time we pop the top from the heap, it costs \log{N}logN time as the size of the heap is O(N).

Space Complexity: O(N), the space used to store our counter cnt and heap h.
"""

class Word:
    def __init__(self, word , occurrence):
        self.word = word
        self.occurrence = occurrence

    def __lt__(self, nxt):
        if(self.occurrence == nxt.occurrence):
            return self.word < nxt.word
        return self.occurrence > nxt.occurrence

class Solution:
    def topKFrequent(self, words, k):
        word_count = {}

        for word in words:
            word_count[word] = word_count.get(word , 0) + 1

        sorted_words = [Word(k,v) for k , v in word_count.items()]

        heapq.heapify(sorted_words)

        i = 1
        result = []
        while k >= i:
            el = heapq.heappop(sorted_words)
            result.append(el.word)
            i += 1

        return result