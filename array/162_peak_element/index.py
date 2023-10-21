from typing import List
"""
No two neighbor elements can be equal.
Ex: Invalid: 1, 2, 2, 3
Ex: Valid: 1, 2, 3 or 3, 2, 1 or 1, 2, 4, 2
"""
# ref: https://www.youtube.com/watch?v=kMzJy9es7Hc
class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            # left neighbor is greater then answer must be in the left side
            if mid > 0 and nums[mid - 1] > nums[mid]:
                r = mid - 1
            # right neighbor is greater then answer must be in the right side
            elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                l = mid + 1
            else:
                return mid
