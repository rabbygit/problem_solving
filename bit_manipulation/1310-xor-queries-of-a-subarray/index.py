from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        res = []
        for n in arr:
            prefix.append(prefix[-1] ^ n)

        for l, r in queries:
            # subtract by xor
            res.append(prefix[r + 1] ^ prefix[l])

        return res
