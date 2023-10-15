from typing import List


# Time Complexity: O(n * 2 ^ n )
class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(sub_result: List[int], i: int):
            # append the sub solution
            result.append(sub_result.copy())

            # loop through every element and find all possibles
            for index in range(i, len(nums)):
                sub_result.append(nums[index])
                backtrack(sub_result, index + 1)
                sub_result.pop()

        backtrack([], 0)

        return result
