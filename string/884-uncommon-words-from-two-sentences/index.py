import collections
from typing import List


class Solution:
    # T.C and S.C: O(n + m)
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1Map = collections.Counter(s1.split(' '))
        s2Map = collections.Counter(s2.split(' '))
        result = []

        for k, v in s1Map.items():
            if v == 1 and k not in s2Map:
                result.append(k)
        
        for k, v in s2Map.items():
            if v == 1 and k not in s1Map:
                result.append(k)

        return result

