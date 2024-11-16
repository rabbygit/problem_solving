from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        r = k
        count = 1
        res = [-1] * (len(nums) - k + 1)

        for i in range(1, k):
            if nums[i - 1] + 1 == nums[i]:
                count += 1

        if count == k:
            res[0] = nums[k - 1]

        for i in range(1, len(nums) - k + 1):
            if nums[i - 1] + 1 == nums[i]:
                count -= 1
            if nums[r - 1] + 1 == nums[r]:
                count += 1

            if count == k:
                res[i] = nums[r]
            r += 1

        return res
