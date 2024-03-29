from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_n = max(nums)
        count = res = l = 0

        for r in range(len(nums)):
            if nums[r] == max_n:
                count += 1

            while count > k or (l <= r and count == k and nums[l] != max_n):
                if nums[l] == max_n:
                    count -= 1
                l += 1

            if count == k:
                res += l + 1

        return res
