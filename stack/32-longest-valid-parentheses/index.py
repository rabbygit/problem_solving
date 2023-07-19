class Solution:

    def longestValidParentheses(self, s: str) -> int:
        stack: list[int] = [-1]
        result = 0

        for i in range(len(s)):
            c = s[i]

            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    result = max(result, i - stack[-1])

        return result
