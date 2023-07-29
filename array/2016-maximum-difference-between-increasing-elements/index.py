class Solution:

    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = -1
        minNum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > minNum:
                maxDiff = max(maxDiff, nums[i] - minNum)
            if minNum > nums[i]:
                minNum = nums[i]

        return maxDiff