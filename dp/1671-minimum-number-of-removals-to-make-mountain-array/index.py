from typing import List


class Solution:
    # T.C: O(n*2) and S.C: O(n)
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1] * n
        lds = [1] * n
        res = n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], 1 + lds[j])

        for i in range(1, n - 1):
            if min(lis[i], lds[i]) > 1:
                res = min(res, n - lis[i] - lds[i] + 1)

        return res
