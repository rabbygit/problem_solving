from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        parentheses_map = {
           '(': ')',
           '{': '}',
           '[': ']'
        }


        for parentheses in s:
            if parentheses in parentheses_map:
                stack.append(parentheses_map[parentheses])
            else:
                if not len(stack) or parentheses != stack.pop():
                    return False

        return len(stack) == 0