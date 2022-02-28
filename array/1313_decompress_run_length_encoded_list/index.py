class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)

        for i in range(0,length,2):
            result.extend([nums[i+1]] * nums[i])
        
        return result