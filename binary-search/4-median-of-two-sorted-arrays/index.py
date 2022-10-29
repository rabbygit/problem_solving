from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:

        x, y = len(nums1), len(nums2)
        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)

        left, right = 0, x
        half = (x + y + 1) // 2

        # run binary search on smaller array
        # and try to find out the partion point
        while left <= right:
            partionX = (left + right) // 2
            partionY = half - partionX

            # left partion might be empty and in that case assign negative infinity
            # because we want the max number from left partion
            maxLeftX = float('-inf') if partionX == 0 else nums1[partionX - 1]
            maxLeftY = float('-inf') if partionY == 0 else nums2[partionY - 1]

            # right partion might be empty and in that case assign positive infinity
            # because we want the min number from right partion
            minRightX = float('inf') if partionX == x else nums1[partionX]
            minRightY = float('inf') if partionY == y else nums2[partionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # found the desired partion of the two array
                # calculate the median
                if ((x + y) % 2)== 0:
                    return (max(maxLeftX, maxLeftY) +
                            min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                # take more element from the second array 
                # because first array's left-most element is bigger
                right = partionX - 1
            else:
                left = partionX + 1