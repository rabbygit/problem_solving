import math


# T.C: O(n)
class Solution:
    def pivotInteger(self, n: int) -> int:
        l = lSum = 1
        r = rSum = n

        while l < r:
            if lSum < rSum:
                l += 1
                lSum += l
            else:
                r -= 1
                rSum += r

        return l if lSum == rSum else -1


# T.C: O(1)
class Solution1:
    # https://assets.leetcode.com/users/images/0f3c0cc2-f982-47aa-8387-54632c23ea34_1710291101.064096.jpeg
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        a = math.sqrt(total)

        if a - math.ceil(a) == 0:
            return int(a)
        else:
            return -1
