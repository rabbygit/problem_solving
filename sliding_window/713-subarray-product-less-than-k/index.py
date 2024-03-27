from typing import List


class Solution:
    # T.C: O(n) and S.C: O(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = l = 0
        product = 1

        for r in range(len(nums)):
            # try to increase the right pointer
            product *= nums[r]
            
            # reduce the window if product is larger
            while product >= k and l <= r:
                product /= nums[l]
                l += 1

            # valid sub-array
            count += r - l + 1

        return count
