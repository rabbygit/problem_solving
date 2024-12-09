from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        parity_count = [1] * len(nums)
        res = []

        for i in range(1, len(nums)):
            if nums[i - 1] % 2 != nums[i] % 2:
                parity_count[i] = parity_count[i - 1] + 1

        for s, e in queries:
            if parity_count[e] >= (e - s + 1):
                res.append(True)
            else:
                res.append(False)

        return res
