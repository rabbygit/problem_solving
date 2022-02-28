class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        result_map = {}
        result = []

        for i in range(len(temp)):
            if temp[i] not in result_map:
                result_map[temp[i]] = i

        for i in range(len(nums)):
            result.append(result_map[nums[i]])

        return result