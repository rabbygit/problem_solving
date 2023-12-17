import collections


class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        nums1Count = collections.Counter(nums1)
        result = []

        for n in nums2:
            if nums1Count[n] > 0:
                result.append(n)
                nums1Count[n] -= 1

        return result