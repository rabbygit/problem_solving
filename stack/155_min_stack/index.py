from typing import List


class MinStack:
    def __init__(self):
        self.stack: List[dict] = []

    def push(self, val: int) -> None:
        current_min = val
        if len(self.stack) and self.stack[-1]['current_min'] < val:
            current_min = self.stack[-1]['current_min']

        self.stack.append({ 'val': val, 'current_min': current_min })

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]['val']

    def getMin(self) -> int:
        return self.stack[-1]['current_min']