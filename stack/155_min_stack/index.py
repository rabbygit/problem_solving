from typing import List


class MinStack:
    def __init__(self):
        self.stack: List[int] = []
        self.min: List[int] = []

    def push(self, val: int) -> None:
        self.setMin(val)
        self.stack.append(val)

    def pop(self) -> None:
        value = self.stack.pop()
        self.popMin(value)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

    def setMin(self, value):
        if not len(self.min) or self.min[-1] >= value:
            self.min.append(value)

    def popMin(self, value):
        if len(self.min) and self.min[-1] == value:
            self.min.pop()
