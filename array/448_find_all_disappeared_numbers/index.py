from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [i+1 for i in range(n)] # construct result array with [1,n] values
        
        for value in nums:
            #  if this value found in result array,that means it's not missing and mark it
            if result[value-1] == value:
                result[value-1] = -1

        # filter found elements
        return list(filter(lambda x: x != -1, result))