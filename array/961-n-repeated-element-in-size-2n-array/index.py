from typing import List


class Solution:

    def repeatedNTimes(self, nums: List[int]) -> int:
        numsMap = {}

        for n in nums:
            if n in numsMap:
                return n

            numsMap[n] = True