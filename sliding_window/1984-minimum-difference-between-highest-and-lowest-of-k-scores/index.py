from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = k + l - 1
        res = float("inf")

        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r = k + l - 1

        return res
