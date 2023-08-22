class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        open = close = 0
        result = ''

        for c in s:
            if c == ')' and close < open:
                result += c
                close += 1
            elif c == '(':
                result += c
                open += 1
            elif c not in '()':
                result += c

        # remove extra opening brackets
        i = len(result) - 1
        open -= close
        while open and i >= 0:
            if result[i] == '(':
                result = result[:i] + result[i + 1:]
                open -= 1
            i -= 1

        return result