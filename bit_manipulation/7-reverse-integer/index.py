import math


class Solution:

    def reverse(self, x: int) -> int:
        result = 0
        MAX_INT = pow(2, 31) - 1  # 2147483647
        MIN_INT = pow(-2, 31)  # -2147483648

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (result > MAX_INT // 10) or (result == MAX_INT // 10
                                            and digit > MAX_INT % 10):
                return 0
            elif (result < MIN_INT // 10) or (result == MIN_INT // 10
                                              and digit < MIN_INT % 10):
                return 0

            result = (result * 10) + digit

        return result