from typing import List


class Solution:
    # T.C & S.C: O(n)
    def findMaxLength(self, nums: List[int]) -> int:
        countMap = {}
        count = maxLen = 0

        for i in range(len(nums)):
            count += 1 if nums[i] else -1
            if count == 0:
                maxLen = i + 1
            elif count in countMap:
                maxLen = max(maxLen, i - countMap[count])
            else:
                countMap[count] = i

        return maxLen
