class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()

        def backtrack(subset, i):
            if i == n:
                result.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(subset, i + 1)
            subset.pop()

            # skip same value to avoid duplicate subset
            # ref:  https://www.youtube.com/watch?v=Vn2v6ajA7U0&t=390s&ab_channel=NeetCode
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1

            backtrack(subset, i + 1)

        backtrack([], 0)

        return result