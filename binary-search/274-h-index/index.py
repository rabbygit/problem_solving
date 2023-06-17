from typing import List


class Solution:
    # https://www.youtube.com/watch?v=CjKJDloMnwE&t=744s&ab_channel=Techdose
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        l, r, mid = 0, n - 1, 0

        while l <= r:
            mid = l + (r - l) // 2

            if citations[mid] == n - mid:
                return citations[mid]
            elif citations[mid] > n - mid:
                r = mid - 1
            else:
                l = mid + 1

        return n - l