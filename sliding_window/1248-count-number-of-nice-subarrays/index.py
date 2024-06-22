from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = oddCount = l = m = 0

        for r in range(len(nums)):
            if nums[r] % 2:
                oddCount += 1

            # invalid window
            # we have to shrink the left and mid pointers
            while oddCount > k:
                if nums[l] % 2:
                    oddCount -= 1
                l += 1
                m = l

            # valid window
            if oddCount == k:
                # go to the first odd number occurance
                # [2(l),2,2,1(m),2,2,1(r)], k = 2
                while nums[m] % 2 == 0:
                    m += 1
                res += m - l + 1

        return res
