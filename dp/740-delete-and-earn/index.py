import collections
from typing import List


class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        nums = sorted(list(set(nums)))
        earn1 = earn2 = 0

        for i in range(len(nums)):
            currEarn = nums[i] * count[nums[i]]
            if i > 0 and nums[i - 1] + 1 == nums[i]:
                tmp = earn2
                earn2 = max(currEarn + earn1, earn2)
                earn1 = tmp
            else:
                tmp = earn2
                earn2 = currEarn + earn2
                earn1 = tmp

        return earn2