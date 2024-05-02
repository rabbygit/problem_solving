from typing import List


class Solution:
    # T.C and S.C: O(n)
    def findMaxK(self, nums: List[int]) -> int:
        maxK = -1
        numsSet = set()

        for n in nums:
            numsSet.add(n)
            if n > 0:
                # positive number check its negative counterpart
                if -n in numsSet:
                    maxK = max(maxK, n)
            else:
                # negative number check its positive counterpart
                if -1 * n in numsSet:
                    maxK = max(maxK, -1 * n)

        return maxK
