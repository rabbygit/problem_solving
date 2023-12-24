import collections


class Solution:

    def reorganizeString(self, s: str) -> str:
        n = len(s)
        charCount = collections.Counter(s)
        maxFreq, mostFreqChar = 0, ''

        for c in charCount:
            if charCount[c] > maxFreq:
                maxFreq, mostFreqChar = charCount[c], c

        if maxFreq - 1 > n - maxFreq:
            return ''

        res = [''] * n
        idx = 0
        for i in range(charCount[mostFreqChar]):
            res[idx] = mostFreqChar
            idx += 2
        charCount[mostFreqChar] = 0

        for c in charCount:
            for j in range(charCount[c]):
                if idx >= n:
                    idx = 1
                res[idx] = c
                idx += 2

        return ''.join(res)