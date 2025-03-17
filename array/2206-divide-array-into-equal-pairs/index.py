import collections
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numsCount = collections.Counter(nums)

        for count in numsCount.values():
            if count % 2:
                return False
        
        return True
        