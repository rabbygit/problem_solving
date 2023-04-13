from typing import List


class Solution:

    # bottom-up approach
    def rob(self, nums: List[int]) -> int:
        nums.append(0)

        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])

        return max(nums[0], nums[1])

    # top-to-bottom approach
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1 ...]
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2