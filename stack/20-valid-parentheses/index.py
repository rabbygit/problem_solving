from typing import List


class Solution:

    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        parentheses_map = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in parentheses_map:
                stack.append(parentheses_map[c])
                continue

            if len(stack) == 0 or c != stack.pop():
                return False

        return len(stack) == 0