# Problem ref: 35. https://leetcode.com/problems/search-insert-position/

import math
# Binary search implementation
def search(nums,left,right,target):
  if right >= left:
      mid = left + math.floor((right-left)/2)

      if nums[mid] == target:
          return mid

      if target < nums[mid]:
          return search(nums,left,mid-1,target)

      return search(nums,mid+1,right,target)

  return left
    
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      return search(nums,0,len(nums)-1,target)
        