import collections
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        charMap = collections.defaultdict(int) # count number of unique appearence
        charMinCount = collections.defaultdict(int) # count min number of appearences in each word
        res = []

        for w in words:
            tempMap = collections.defaultdict(int)
            for c in w:
                if c not in tempMap:
                    charMap[c] += 1
                tempMap[c] += 1

            for k, v in tempMap.items():
                if k in charMinCount:
                    charMinCount[k] = min(charMinCount[k], v)
                else:
                    charMinCount[k] = v

        # build the result
        for k, v in charMap.items():
            if v == len(words):
                for _ in range(charMinCount[k]):
                    res.append(k)

        return res
