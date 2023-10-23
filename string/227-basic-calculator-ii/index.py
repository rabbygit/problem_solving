class Solution:

    def calculate(self, s: str) -> int:
        idx = prev = curr = res = 0
        last_op = '+'

        while idx < len(s):
            char = s[idx]
            if char.isdigit():
                while idx < len(s) and s[idx].isdigit():
                    curr = curr * 10 + int(s[idx])
                    idx += 1
                idx -= 1
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
            elif char != ' ':
                last_op = char
            idx += 1

        return res
