import bisect
from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

# T.C: O(n logn)
# S.C: O(n)
class Solution1:
    # ref: https://leetcode.com/problems/longest-increasing-subsequence/solutions/4509317/greedy-with-binary-search-beats-99-33-users/
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]
        for x in nums[1:]:
            if x > lis[-1]:
                lis.append(x)
            else:
                i = bisect.bisect_left(lis, x)
                lis[i] = x
        return len(lis)
