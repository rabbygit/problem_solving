from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open, close, str):
            if open == close == n:
                result.append(str)
                return

            if open < n:
                backtrack(open + 1, close, str + '(')

            if close < open:
                backtrack(open, close + 1, str + ')')

        backtrack(0, 0, '')
        return result