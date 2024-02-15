from typing import List


class Solution1:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        result, prefixSum = -1, 0

        for n in nums:
            if prefixSum > n:
                result = prefixSum + n
            prefixSum += n

        return result


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        pre = 0
        prefixSum = [0] * len(nums)

        for i in range(len(nums)):
            prefixSum[i] = pre + nums[i]
            pre = prefixSum[i]

        for r in range(len(nums) - 1, -1, -1):
            if r >= 2 and prefixSum[r - 1] > nums[r]:
                return prefixSum[r]

        return -1
