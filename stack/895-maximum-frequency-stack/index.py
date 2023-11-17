class FreqStack:

    def __init__(self):
        self.maxCount = 0
        self.stackMap = {}
        self.countMap = {}

    def push(self, val: int) -> None:
        count = self.countMap.get(val, 0) + 1

        if count > self.maxCount:
            self.maxCount += 1
            self.stackMap[count] = []

        self.countMap[val] = count
        self.stackMap[count].append(val)

    def pop(self) -> int:
        res = self.stackMap[self.maxCount].pop()
        self.countMap[res] -= 1
        if not self.stackMap[self.maxCount]:
            self.maxCount -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()