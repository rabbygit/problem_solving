from collections import defaultdict
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(i: int, numsMap):
            if i == len(nums):
                return 1

            res = dfs(i + 1, numsMap)

            if not numsMap[nums[i] + k] and not numsMap[nums[i] - k]:
                numsMap[nums[i]] += 1
                res += dfs(i + 1, numsMap)
                numsMap[nums[i]] -= 1

            return res

        return dfs(0, defaultdict(int)) - 1
