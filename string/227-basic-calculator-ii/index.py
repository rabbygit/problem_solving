class Solution:

    def calculate(self, s: str) -> int:
        l, prev, curr, res, last_op = 0, 0, 0, 0, '+'

        while l < len(s):
            if s[l].isdigit():
                while l < len(s) and s[l].isdigit():
                    curr = curr * 10 + int(s[l])
                    l += 1
                l -= 1
                if last_op == '+':
                    res += curr
                    prev = curr
                elif last_op == '-':
                    res -= curr
                    prev = -curr
                elif last_op == '*':
                    res -= prev
                    res += prev * curr
                    prev = prev * curr
                elif last_op == '/':
                    res -= prev
                    res += int(prev / curr)
                    prev = int(prev / curr)
                curr = 0
            elif s[l] != ' ':
                last_op = s[l]
            l += 1

        return res
