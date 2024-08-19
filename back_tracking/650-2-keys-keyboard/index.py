class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        cache = {}

        def helper(count, paste):
            if count == n:
                return 0
            elif count > n:
                return 1000
            elif (count, paste) in cache:
                return cache[(count, paste)]

            res1 = 1 + helper(count + paste, paste)
            res2 = 2 + helper(count + count, count)
            cache[(count, paste)] = min(res1, res2)

            return cache[(count, paste)]

        return 1 + helper(1, 1)
