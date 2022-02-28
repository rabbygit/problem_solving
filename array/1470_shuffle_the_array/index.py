class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        result = [False] * n
        j = n//2
        k = 0 
        
        for i in range(n//2):
            result[k] = nums[i]
            result[k+1] = nums[j]
            
            k += 2
            j += 1
            
        return result