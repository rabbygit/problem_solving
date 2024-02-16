import collections
import heapq
from typing import List


# class Solution:
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     if len(s) != len(t): return False

    #     sCount = collections.Counter(s)
    #     tCount = collections.Counter(t)
    #     sOccur = collections.defaultdict(int)
    #     tOccur = collections.defaultdict(int)

    #     for k, v in sCount.items():
    #         sOccur[v] += 1
    #     for k, v in tCount.items():
    #         tOccur[v] += 1

    #     for k, v in sOccur.items():
    #         if k not in tOccur or v != tOccur[k]:
    #             return False
        
    #     return True


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        minHeap = sorted(collections.Counter(arr).values(), reverse=True)
        while k > 0:
            k -= minHeap.pop()
        return len(minHeap) + 1 if k < 0 else len(minHeap)