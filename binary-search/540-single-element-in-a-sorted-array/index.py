from typing import List


class Solution:

    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            # determine if this is the single item
            if m + 1 >= len(nums) and nums[m - 1] != nums[m]:
                return nums[m]
            elif m - 1 < 0 and nums[m + 1] != nums[m]:
                return nums[m]
            elif nums[m - 1] != nums[m] and nums[m + 1] != nums[m]:
                return nums[m]

            # move to the odd number size elements
            leftSize = m
            if m - 1 >= 0 and nums[m - 1] == nums[m]:
                leftSize = m - 1

            if leftSize % 2:
                r = m - 1
            else:
                l = m + 1