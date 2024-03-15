import collections
from typing import List


class Solution1:
    # T.C: O(n) and S.C: O(n)
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sumCount = collections.defaultdict(int)
        sumCount[0] = 1
        res = pSum = 0

        for n in nums:
            pSum += n

            if pSum - goal in sumCount:
                res += sumCount[pSum - goal]

            sumCount[pSum] += 1

        return res

# T.C: O(n) and S.C: O(1)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def countSubArray(g):
            if g < 0:
                return 0
            res = l = curr = 0
            for r in range(len(nums)):
                curr += nums[r]
                while curr > g:
                    curr -= nums[l]
                    l += 1
                res += r - l + 1
            return res

        return countSubArray(goal) - countSubArray(goal - 1)
