class Solution:
    # T.C: O(log n) and S.C: O(1)
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1

        l, r = 1, n
        while l < r:
            m = l + (r - l) // 2
            used = m * ((m + 1) / 2)

            if used > n:
                r = m
            else:
                l = m + 1

        return l - 1
