from typing import List


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        idx = len(nums) - 1
        result = [0] * len(nums)

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result[idx] = nums[l] * nums[l]
                l += 1
            else:
                result[idx] = nums[r] * nums[r]
                r -= 1
            idx -= 1

        return result