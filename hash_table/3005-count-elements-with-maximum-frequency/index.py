import collections
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqCount = collections.defaultdict(int)
        maxFreq = 0
        maxFreqCount = 1
        
        for n in nums:
            freqCount[n] += 1
            if freqCount[n] > maxFreq:
                maxFreqCount = 1
                maxFreq = freqCount[n]
            elif freqCount[n] == maxFreq:
                maxFreqCount += 1

        return maxFreqCount * maxFreq