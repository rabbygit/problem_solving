import collections
import random


class RandomizedCollection:

    def __init__(self):
        self.numsMap = collections.defaultdict(set)
        self.numsList = []

    def insert(self, val: int) -> bool:
        self.numsList.append(val)
        self.numsMap[val].add(len(self.numsList) - 1)
        return len(self.numsMap[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.numsMap[val]:
            return False

        lastVal = self.numsList[-1]
        idx = self.numsMap[val].pop()
        self.numsList[idx] = lastVal
        self.numsMap[lastVal].add(idx)
        self.numsMap[lastVal].discard(len(self.numsList) - 1)
        self.numsList.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.numsList)