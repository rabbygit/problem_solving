class Solution:

    def calculate(self, s: str) -> int:
        output, curr, stack = 0, 0, []
        lastSign = 1

        for c in s:
            if c.isdigit():
                curr = curr * 10 + int(c)
            elif c in '+-':
                output += curr * lastSign
                curr = 0
                lastSign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(output)
                stack.append(lastSign)
                output = 0
                lastSign = 1
            elif c == ')':
                output += curr * lastSign
                output *= stack.pop()
                output += stack.pop()
                curr = 0

        return output + curr * lastSign
