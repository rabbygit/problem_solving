from typing import List


class Solution:
    # T.C: O(n) and S.C: O(1)
    def longestSubarray(self, nums: List[int]) -> int:
        curr_max = size = res = 0

        # AND of equal number is the same number. 5 & 5 = 5
        # AND of two different number is smaller than the bigger number.
        # so, to find the longest subarray of AND, we have to find the max number's subarray
        for n in nums:
            if n > curr_max:
                curr_max = n
                size = 1
                res = 1
            elif n == curr_max:
                size += 1
                res = max(res, size)
            else:
                size = 0

        return res
