from typing import List


class Solution:
    # T.C and S.C: O(n)
    def longestSquareStreak(self, nums: List[int]) -> int:
        cache = {}
        numsSet = set(nums)
        longestLen = 0

        def dfs(num: int) -> int:
            if num not in numsSet:
                return 0
            if num in cache:
                return cache[num]

            cache[num] = 1 + dfs(num * num)
            return cache[num]

        for n in nums:
            longestLen = max(longestLen, dfs(n))

        return -1 if longestLen < 2 else longestLen
