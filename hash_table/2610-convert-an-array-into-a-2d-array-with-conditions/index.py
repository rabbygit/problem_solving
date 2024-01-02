import collections
from typing import List


class Solution:

    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numsOccurrence = collections.defaultdict(int)
        maxOccurrence = 0

        for n in nums:
            numsOccurrence[n] += 1
            maxOccurrence = max(maxOccurrence, numsOccurrence[n])

        result = [[] for _ in range(maxOccurrence)]

        for n, occurrence in numsOccurrence.items():
            for idx in range(occurrence):
                result[idx].append(n)

        return result


class Solution1:

    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numsCounter = collections.defaultdict(int)
        result = []

        for n in nums:
            row = numsCounter[n]

            if row == len(result):
                result.append([])

            result[row].append(n)
            numsCounter[n] += 1

        return result
