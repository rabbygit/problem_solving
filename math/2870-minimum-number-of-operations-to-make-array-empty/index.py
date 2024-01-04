import math
import collections
from typing import List


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        numsCounter = collections.Counter(nums)
        operations = 0

        for occur in numsCounter.values():
            if occur == 1:
                return -1
            else:
                operations += math.ceil(occur / 3)

        return operations