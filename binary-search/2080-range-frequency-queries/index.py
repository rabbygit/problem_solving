from bisect import bisect_left, bisect_right
import collections
from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.numsMap = collections.defaultdict(list)
        for idx, num in enumerate(arr):
            self.numsMap[num].append(idx)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect_right(self.numsMap[value], right) - bisect_left(
            self.numsMap[value], left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)