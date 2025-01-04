import collections


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = collections.Counter(s)

        for m in s:
            right[m] -= 1

            for leftChar in left:
                if right[leftChar] > 0:
                    res.add((leftChar, m))

            left.add(m)

        return len(res)
