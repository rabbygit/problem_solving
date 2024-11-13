from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        nums.sort()

        def search(l, r, t):
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] >= t:
                    r = m - 1
                else:
                    l = m + 1
            return r

        for i in range(len(nums)):
            up = upper - nums[i]
            lo = lower - nums[i]
            l, r = i + 1, len(nums) - 1
            res += search(l, r, up + 1) - search(l, r, lo)

        return res
