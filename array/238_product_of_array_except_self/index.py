class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]

        # calculate prefix product upto each position
        for index in range(len(nums)):
            result.append(nums[index] * result[index])

        # calculate suffix product upto each position and 
        # multiply with the prefix product
        nums.append(1)
        for index in range(len(nums)-2 , -1, -1):
            nums[index] = nums[index] * nums[index + 1]
            result[index] = result[index] * nums[index + 1]

        result.pop()
        return result