import collections
from typing import List


class Solution:
    # T.C and S.C: O(n)
    def countGood(self, nums: List[int], k: int) -> int:
        numsMap = collections.defaultdict(int)
        count = pair = 0
        r = -1
        n = len(nums)

        for l in range(n):
            while pair < k and r + 1 < n:
                r += 1
                pair += numsMap[nums[r]]
                numsMap[nums[r]] += 1
                
            if pair >= k:
                count += n - r

            numsMap[nums[l]] -= 1
            pair -= numsMap[nums[l]]

        return count
