from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivots = []
        lessNums = []
        greaterNums = []

        for n in nums:
            if n < pivot:
                lessNums.append(n)
            elif n > pivot:
                greaterNums.append(n)
            else:
                pivots.append(n)

        return lessNums + pivots + greaterNums


class Solution2:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i, j = 0, len(nums) - 1
        i2, j2 = 0, len(nums) - 1
        res = [0] * len(nums)

        while i < len(nums):
            if nums[i] < pivot:
                res[i2] = nums[i]
                i2 += 1
            if nums[j] > pivot:
                res[j2] = nums[j]
                j2 -= 1
            i += 1
            j -= 1

        while i2 <= j2:
            res[i2] = pivot
            i2 += 1

        return res
