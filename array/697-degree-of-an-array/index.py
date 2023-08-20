class Solution:

    def findShortestSubArray(self, nums: List[int]) -> int:
        numsMap = {}
        shortestLen = maxDegree = 0

        for i, n in enumerate(nums):
            prev = numsMap.get(n, {'firstOccur': i, 'totalOccur': 0})
            prev['totalOccur'] += 1
            numsMap[n] = prev

            if prev['totalOccur'] > maxDegree:
                maxDegree = prev['totalOccur']
                shortestLen = i - prev['firstOccur'] + 1
            elif prev['totalOccur'] == maxDegree:
                shortestLen = min(shortestLen, i - prev['firstOccur'] + 1)

        return shortestLen