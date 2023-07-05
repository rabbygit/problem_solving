from typing import List


class Solution:

    def decodeString(self, s: str) -> str:
        stack: List[str] = []

        for i in range(len(s)):
            char = s[i]
            if char != ']':
                stack.append(char)
            else:
                substr = ''
                k = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()  # pop the '['
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)

        return "".join(stack)
