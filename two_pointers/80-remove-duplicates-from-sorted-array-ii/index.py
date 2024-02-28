from typing import List


class Solution:
    # T.C: O(n) and S.C: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0

        while r < len(nums):
            duplicate = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                duplicate += 1

            for i in range(min(2, duplicate)):
                nums[l] = nums[r]
                l += 1

            r += 1

        return l
