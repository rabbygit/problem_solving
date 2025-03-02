from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        res = []
        i = j = 0
        length1, length2 = len(nums1), len(nums2)

        while i < length1 and j < length2:
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1]])
                i += 1
            else:
                res.append([nums2[j][0], nums2[j][1]])
                j += 1

        while i < length1:
            res.append([nums1[i][0], nums1[i][1]])
            i += 1

        while j < length2:
            res.append([nums2[j][0], nums2[j][1]])
            j += 1

        return res
