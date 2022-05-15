class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        index = 0
        result = []
        nums.sort()

        if n < 3:
            return result

        while index < n - 2:
            left = index + 1
            right = n - 1

            while left < right:
                sum = nums[index] + nums[left] + nums[right]

                if sum == 0:
                    result.append([nums[index], nums[left], nums[right]])

                    while nums[left] == nums[left + 1] and left < right - 1:
                        left += 1

                    while nums[right] == nums[right - 1] and left < right - 1:
                        right -= 1

                    left += 1

                elif sum > 0:
                    right -= 1
                else:
                    left += 1

            while index < n - 3 and nums[index] == nums[index + 1]:
                index += 1

            index += 1

        return result
