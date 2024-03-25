from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            idx = abs(n) - 1

            if nums[idx] < 0:
                res.append(idx + 1)

            nums[idx] = -nums[idx]

        return res
