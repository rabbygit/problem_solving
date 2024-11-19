import collections
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = l = curr = 0
        numsSet = collections.defaultdict(int)

        for r in range(len(nums)):
            curr += nums[r]
            numsSet[nums[r]] += 1

            if r - l + 1 > k:
                numsSet[nums[l]] -= 1
                if numsSet[nums[l]] == 0:
                    numsSet.pop(nums[l])
                curr -= nums[l]
                l += 1

            if len(numsSet) == r - l + 1 == k:
                res = max(res, curr)

        return res
