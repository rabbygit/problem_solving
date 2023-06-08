import random


class RandomizedSet:

    def __init__(self):
        self.numsMap = {}
        self.numsList = []

    def insert(self, val: int) -> bool:
        result = val not in self.numsMap

        if result:
            self.numsList.append(val)
            self.numsMap[val] = len(self.numsList) - 1

        return result

    def remove(self, val: int) -> bool:
        result = val in self.numsMap

        if result:
            idx = self.numsMap[val]
            lastVal = self.numsList[-1]
            self.numsList[idx] = lastVal
            self.numsList.pop()
            self.numsMap[lastVal] = idx
            del self.numsMap[val]

        return result

    def getRandom(self) -> int:
        return random.choice(self.numsList)