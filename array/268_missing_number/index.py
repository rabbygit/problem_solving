from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n+1) / 2 # summation of sequence numbers ex: 1+2+3+..
        total = 0
        
        # loop thhrugh every number and calculate total sum
        for i in nums:
            total += i
        
        # subtraction result is the missing number
        return int(total_sum - total)