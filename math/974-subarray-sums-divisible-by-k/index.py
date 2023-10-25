import collections
from typing import List


class Solution:

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = currSum = 0
        reminders = collections.defaultdict(int)
        reminders[0] = 1

        for n in nums:
            currSum += n
            res += reminders[currSum % k]
            reminders[currSum % k] += 1

        return res