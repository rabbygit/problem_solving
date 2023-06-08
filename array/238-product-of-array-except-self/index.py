class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefixProd = 1
        suffixProd = 1

        # calculate prefix product upto each position
        for i in range(len(nums)):
            result[i] = prefixProd
            prefixProd *= nums[i]

        # calculate suffix product upto each position and
        # multiply with the prefix product
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffixProd
            suffixProd *= nums[i]

        return result