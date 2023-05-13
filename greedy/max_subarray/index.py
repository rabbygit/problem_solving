# Problem Ref: 53. https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        
        if length==1:
          return nums[0]
        
        max = nums[0]
        sum = 0
        min= 0
        
        for index in range(length):
          sum += nums[index]
          if sum - min > max:
            max = sum - min
          if sum < min:
            min = sum
            
        return max