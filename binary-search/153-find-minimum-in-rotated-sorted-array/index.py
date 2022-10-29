import math
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = math.inf
        left , right = 0 , len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            minNum = min(minNum , nums[mid])

            if nums[left] <= nums[mid]:
                if nums[right] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[right] > nums[mid] or nums[right] > nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return minNum

