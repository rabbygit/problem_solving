class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxSum = nums[0]

        for i in range(1, len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[i]
            maxSum = max(maxSum, currSum)

        return maxSum