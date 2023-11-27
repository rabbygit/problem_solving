from typing import List


class Solution:

    def minMoves(self, nums: List[int]) -> int:
        res = 0
        minNum = min(nums)

        for n in nums:
            res += n - minNum

        return res


# another solution
class Solution2():
    # ref1: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/solutions/93817/it-is-a-math-question/
    # ref2: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/solutions/93817/it-is-a-math-question/comments/98130
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sum = sum of all items in nums
        # m   = number of moves
        # x   = value of all items in nums after m moves
        # n   = number of items in nums
        # x*n = sum of all items after m moves
        # each move add (n-1) to sum
        # so m moves add m*(n-1) to sum
        # so x*n = sum + m*(n - 1) ............. (1)

        # smallest is smallest number in nums before moves, after m moves, m got added to it and it became x
        # smallest + m = x  ............... (2)

        # smallest * n + m*n = sum + m*n - m.................using (1) and (2)
        # smallest * n       = sum - m ............ m*n cancel on both side
        # m  = sum - smallest * n .......... m (final desired result)
        m = 0
        if nums:
            n = len(nums)
            smallest = min(nums)
            m = sum(nums) - smallest * n
        return m