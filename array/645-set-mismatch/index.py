from typing import List


class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate, missing = 0, len(nums)

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                duplicate = idx + 1
            else:
                # mark the index as visited with negative value
                nums[idx] = -1 * nums[idx]

        # now, index having positive value is the missing number
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1

        return [duplicate, missing]
