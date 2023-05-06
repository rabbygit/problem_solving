class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}  # (index, sum) -> total number of ways

        def dfs(index, sum):
            if index == len(nums):
                return 1 if sum == target else 0
            if (index, sum) in cache:
                return cache[(index, sum)]

            # now we have two choices.
            # 1. Adding the current number or
            # 2. Subtracting the current number
            cache[(index, sum)] = dfs(index + 1, sum + nums[index]) + dfs(
                index + 1, sum - nums[index])

            return cache[(index, sum)]

        return dfs(0, 0)
