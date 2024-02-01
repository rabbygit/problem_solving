from typing import List


class Solution:
    # Intuition: Use monotonic increasing stack to get the sorting order of elements 
    # without actually sorting the array.
    # https://www.youtube.com/watch?v=YLesLbNkyjA
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res, stack, prefix = 0, [], [0]

        for n in nums:
            prefix.append(prefix[-1] + n)

        for i, n in enumerate(nums):
            startIdx = i

            while stack and stack[-1][1] > n:
                start, value = stack.pop()
                total = value * (prefix[i] - prefix[start])
                res = max(res, total)
                startIdx = start

            stack.append([startIdx, n])

        for start, value in stack:
            total = value * (prefix[len(nums)] - prefix[start])
            res = max(res, total)

        return res % (10**9 + 7)