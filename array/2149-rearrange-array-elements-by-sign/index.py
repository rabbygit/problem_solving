from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pIdx = 0
        nIdx = 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > -1:
                res[pIdx] = nums[i]
                pIdx += 2
            else:
                res[nIdx] = nums[i]
                nIdx += 2

        return res

class Solution1:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        res = []

        for n in nums:
            if n > -1:
                positive.append(n)
            else:
                negative.append(n)

        for p, n in zip(positive, negative):
            res.append(p)
            res.append(n)

        return res