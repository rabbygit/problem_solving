from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for token in tokens:
            if not is_number(token):
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(self.evaluate(num1, num2, token))
            else:
                numStack.append(int(token))

        return numStack.pop()

    def evaluate(self, num1, num2, operand):
        if operand == '+':
            return (num2 + num1)
        elif operand == '-':
            return num2 - num1
        elif operand == '*':
            return num2 * num1
        else:
            return int(num2 / num1)


def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True