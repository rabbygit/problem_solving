import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        res = ''
        count = collections.Counter(s)
        freqMap = collections.defaultdict(list)
        
        for char, occur in count.items():
            freqMap[occur].append(char)

        for i in range(len(s), -1, -1):
            for c in freqMap[i]:
                res += c * i
        
        return res
   