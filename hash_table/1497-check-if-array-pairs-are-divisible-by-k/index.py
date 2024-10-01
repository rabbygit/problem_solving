import collections
from typing import List


class Solution:
    # T.C and S.C: O(n)
    def canArrange(self, arr: List[int], k: int) -> bool:
        pairCount = 0
        reminderMap = collections.defaultdict(int)

        for n in arr:
            reminder = n % k

            # negative number, adding k will give the correct reminder
            if reminder < 0:
                reminder += k

            # found a pair
            if reminder in reminderMap:
                pairCount += 1
                reminderMap[reminder] -= 1
                if reminderMap[reminder] == 0:
                    del reminderMap[reminder]
            else:
                if reminder == 0:
                    reminderMap[0] += 1
                else:
                    reminderMap[k - reminder] += 1

        return len(arr) // 2 == pairCount
