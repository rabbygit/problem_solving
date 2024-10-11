import heapq
from typing import List


class Solution:
    # T.C: O(n logn) and S.C: O(n)
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        timesIdx = [(t[0], t[1], i) for i, t in enumerate(times)]
        timesIdx.sort()

        available = [i for i in range(len(times))]  # [0,1,2] chairs
        used = []  # [(l, chair)]

        for a, l, idx in timesIdx:
            while used and used[0][0] <= a:
                leave, chair = heapq.heappop(used)
                heapq.heappush(available, chair)

            chair = heapq.heappop(available)
            heapq.heappush(used, (l, chair))

            if idx == targetFriend:
                return chair

        return -1
