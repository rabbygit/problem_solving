class Solution:

    def canJump(self, nums: List[int]) -> bool:
        destination = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= destination:
                destination = i

        return True if destination == 0 else False