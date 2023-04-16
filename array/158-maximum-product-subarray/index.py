class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            tempMax = n * curMax
            tempMin = n * curMin
            curMax = max(tempMax, tempMin, n)
            curMin = min(tempMax, tempMin, n)
            result = max(result, curMax)

        return result