from typing import List


class Solution:
    # T.C: O(n) and S.C: O(1)
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftSum = nums[0]
        rightSum = 0
        res = 0

        for i in range(1, len(nums)):
            rightSum += nums[i]

        for i in range(1, len(nums)):
            if leftSum >= rightSum:
                res += 1

            leftSum += nums[i]
            rightSum -= nums[i]

        return res
