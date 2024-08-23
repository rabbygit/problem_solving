import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator = 0
        denominator = 1
        i = 0
        sign = 1

        while i < len(expression):
            num = 0
            denum = 0

            # determine sign
            if expression[i] == "+":
                sign = 1
                i += 1
            elif expression[i] == "-":
                sign = -1
                i += 1

            # determine current fraction's numerator
            while expression[i] != "/":
                num = num * 10 + int(expression[i])
                i += 1

            # determine current fraction's denominator
            i += 1
            while i < len(expression) and expression[i] not in ["+", "-"]:
                denum = denum * 10 + int(expression[i])
                i += 1

            # perform cross multiplication
            numerator = (numerator * denum) + sign * (denominator * num)
            denominator = denominator * denum

        cmn_divisor = math.gcd(numerator, denominator)
        return f"{numerator // cmn_divisor}/{denominator // cmn_divisor}"
