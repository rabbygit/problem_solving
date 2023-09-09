import collections
from typing import List


class Solution:
    # Time: O(N + S),
    # where N <= 5*10^4 is length of string s
    # S <= 5000*50 is sum length of all words
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        total, wordMap = 0, collections.defaultdict(list)

        for word in words:
            wordMap[word[0]].append(word)

        for char in s:
            expectingCharWords = wordMap[char]
            wordMap[char] = []
            for word in expectingCharWords:
                if len(word) == 1:
                    total += 1
                else:
                    wordMap[word[1]].append(word[1:])

        return total