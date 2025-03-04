class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(i, curr) -> bool:
            if curr == n:
                return True
            if 3**i > n or curr > n:
                return False

            if backtrack(i + 1, curr + 3**i):
                return True
            return backtrack(i + 1, curr)

        return backtrack(0, 0)


class Solution1:
    def checkPowersOfThree(self, n: int) -> bool:
        i = 0
        # find the max possible power of 3
        while 3**i <= n:
            i += 1

        i -= 1

        # remove largest power
        while i >= 0:
            power = 3**i
            if power <= n:
                n -= power
            i -= 1

        return n == 0
