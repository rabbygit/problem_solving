import collections
import heapq


class Solution:
    # T.C: O(n * log k)
    # In the worst case, we perform two heap operations for every character in the string,
    # resulting in O(N) heap operations.
    # Each heap operation involves pushing or popping an element,
    # which takes O(logK) time.
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = collections.Counter(s)
        maxHeap = [[-ord(ch), cnt] for ch, cnt in count.items()]
        heapq.heapify(maxHeap)
        res = []

        while maxHeap:
            ch, cnt = heapq.heappop(maxHeap)
            ch = chr(-ch)
            allowdCnt = min(cnt, repeatLimit)
            res.append(ch * allowdCnt)

            if cnt > repeatLimit and maxHeap:
                next_ch, next_cnt = heapq.heappop(maxHeap)
                next_ch = chr(-next_ch)
                res.append(next_ch)
                if next_cnt > 1:
                    heapq.heappush(maxHeap, [-ord(next_ch), next_cnt - 1])
                heapq.heappush(maxHeap, [-ord(ch), cnt - repeatLimit])

        return "".join(res)
