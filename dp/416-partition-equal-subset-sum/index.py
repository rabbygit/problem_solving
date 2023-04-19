class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        dp = set()
        dp.add(0)
        target = total // 2

        if total % 2:
            return False

        for i in range(len(nums) - 1, -1, -1):
            nextDp = dp.copy()

            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDp.add(t + nums[i])

            dp = nextDp

        return False
