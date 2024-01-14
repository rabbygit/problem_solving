import collections


class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1Frequency = [0] * len(word1)
        word2Frequency = [0] * len(word1)
        word1Count = collections.Counter(word1)
        word2Count = collections.Counter(word2)

        for k, v in word1Count.items():
            if k not in word2Count: return False
            word1Frequency[v - 1] += 1

        for k, v in word2Count.items():
            if k not in word1Count: return False
            word2Frequency[v - 1] += 1

        for freq1, freq2 in zip(word1Frequency, word2Frequency):
            if freq1 != freq2: return False

        return True
