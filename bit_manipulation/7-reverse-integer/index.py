import math


class Solution:

    def reverse(self, x: int) -> int:
        result = 0
        MAX_INT_ONE_DIGIT_LESS = 214748364  #  MAX_INT -> 2147483647
        MIN_INT_ONE_DIGIT_LESS = -214748364  # MIN_INT -> -2147483648

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (result > MAX_INT_ONE_DIGIT_LESS) or (
                    result == MAX_INT_ONE_DIGIT_LESS and digit > 7):
                return 0
            elif (result < MIN_INT_ONE_DIGIT_LESS) or (
                    result == MIN_INT_ONE_DIGIT_LESS and digit < -8):
                return 0

            result = (result * 10) + digit

        return result