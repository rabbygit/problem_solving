from typing import List


class Solution:

    def minMoves(self, nums: List[int]) -> int:
        res = 0
        minNum = min(nums)

        for n in nums:
            res += n - minNum

        return res