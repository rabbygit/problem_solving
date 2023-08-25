import random


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        total = sum(self.w)

        for i in range(len(self.w)):
            self.w[i] = self.w[i] / total

        for i in range(1, len(self.w)):
            self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:
        possbility = random.uniform(0, 1)

        for idx, num in enumerate(self.w):
            if possbility <= num:
                return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()