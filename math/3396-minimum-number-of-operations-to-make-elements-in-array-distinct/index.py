import math
from typing import List

class Solution:
    # T.C: O(n) and S.C: O(n)
    def minimumOperations(self, nums: List[int]) -> int:
        firstDuplicateIdx = 0
        numsSet = set()
        numsSet.add(nums[-1])

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] in numsSet:
                firstDuplicateIdx = i
                return math.ceil((firstDuplicateIdx + 1) / 3)
            else:
                numsSet.add(nums[i])

        return 0
