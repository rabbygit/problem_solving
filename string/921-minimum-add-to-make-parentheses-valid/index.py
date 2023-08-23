class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        result = open = close = 0

        for c in s:
            if c == ')':
                close += 1
                if close > open:
                    open += 1
                    result += 1
            else:
                open += 1

        # count extra opening brackets
        result += open - close

        return result