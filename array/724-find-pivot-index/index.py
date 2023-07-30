class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)

        for idx, num in enumerate(nums):
            rightSum -= num

            if leftSum == rightSum:
                return idx

            leftSum += num

        return -1