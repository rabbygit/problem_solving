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

    def longestValidParentheses2(self, s: str) -> int:
        maxLen = l = r = 0

        for c in s:
            if c == '(': l += 1
            else: r += 1

            if l == r:
                maxLen = max(maxLen, l * 2)
            elif r > l:
                l = r = 0

        l = r = 0
        # "(()"
        for i in range(len(s) - 1, -1, -1):
            c = s[i]

            if c == '(': l += 1
            else: r += 1

            if l == r:
                maxLen = max(maxLen, l * 2)
            elif l > r:
                l = r = 0

        return maxLen
