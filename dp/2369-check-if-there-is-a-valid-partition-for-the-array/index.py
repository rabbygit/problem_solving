from typing import List


class Solution:

    def validPartition(self, nums: List[int]) -> bool:
        dp = {}
        n = len(nums)

        def dfs(i):
            if i == n:
                return True
            if i in dp:
                return dp[i]

            res = False
            if i + 1 < n and nums[i] == nums[i + 1]:
                res = dfs(i + 2)
            if i + 2 < n and nums[i] == nums[i + 1] == nums[i + 2]:
                res = res or dfs(i + 3)
            if i + 2 < n and nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1:
                res = res or dfs(i + 3)
                
            dp[i] = res
            return res

        return dfs(0)
