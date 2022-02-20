from cgitb import reset


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            # xor operation returns 0 if both bits are same and 1 for different bits
            # so, if we xor two same number it will return 0 and after that xor with unique number
            # it will give the unique number
            # Ex: [2,2,1] 010 ^ 010 = 000 ^ 001 = 001 
            result = result ^ num
        
        return result