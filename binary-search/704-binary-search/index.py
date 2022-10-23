from operator import le
from typing import List


class Solution:

    # recursive approach
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(start, end):

            if start > end:
                return -1

            mid = (end + start) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return binarySearch(mid + 1, end)
            else:
                return binarySearch(start, mid - 1)

        return binarySearch(0, len(nums) - 1)

    # iterative approach
    def iterativeBinaryearch(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while end >= start:
            mid = (end + start) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return -1