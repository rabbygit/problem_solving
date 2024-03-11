import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charCount = collections.Counter(s)
        res = []

        for char in order:
            # add characters maintaining the order
            if charCount[char]:
                res.append(charCount[char] * char)
                del charCount[char]

        # add characters that only present in "s"
        for k, v in charCount.items():
            res.append(k * v)

        return "".join(res)