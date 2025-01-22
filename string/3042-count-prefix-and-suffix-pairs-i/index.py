from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixSuffixPairs(word1: str, word2: str) -> bool:
            n1 = len(word1)
            n2 = len(word2)
            if n2 < n1:
                return False

            return word1 == word2[:n1] == word2[n2 - n1 :]

        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixSuffixPairs(words[i], words[j]):
                    res += 1
        return res
