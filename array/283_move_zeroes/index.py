from operator import index, le
import re


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        replace_idx = 0
        n = len(nums)

        for index in range(n):
            if nums[index] != 0:
                if replace_idx != index:
                    nums[replace_idx] = nums[index]
                    nums[index] = 0

                replace_idx += 1
