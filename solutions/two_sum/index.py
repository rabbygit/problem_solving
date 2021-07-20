# Problem ref: 1. https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
  result = []
  my_dict = {}
  
  # loop through the whole array
  for index in range(len(nums)):
    # get the remaining value by subtracting index value from target
    value = target - nums[index]
    
    # check if the value exists in dictionary
    if value in my_dict:
      result = [my_dict[value],index]
      break
    else:
      my_dict[nums[index]] = index

  return result