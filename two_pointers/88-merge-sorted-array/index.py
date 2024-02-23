from typing import List


class Solution:
    # time complexity: O(m + n)
    # space complexity: O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1
        m -= 1
        n -= 1

        # merge from the end since "the last n elements are set to 0"
        # nums1 = [1,2,3,0,0,0], nums2 = [2,5,6]
        while m >= 0 and n >= 0:
            if nums2[n] > nums1[m]:
                nums1[idx] = nums2[n]
                n -= 1
            else:
                nums1[idx] = nums1[m]
                m -= 1
            idx -= 1

        # merge the remaining form nums2
        while n >= 0:
            nums1[idx] = nums2[n]
            n -= 1
            idx -= 1
