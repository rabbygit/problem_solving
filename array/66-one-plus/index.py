# Problem ref: 66. https://leetcode.com/problems/plus-one/submissions/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      hold = 1
      
      for index in range(len(digits),0,-1):
        sum = digits[index-1] + hold
        if sum == 10:
          digits[index-1] = 0
          hold = 1
        else:
          digits[index-1] = sum
          hold = 0
      
      if hold:
        digits.insert(0,1)
        
      return digits