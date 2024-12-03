from typing import List


class Solution:
    # T.C and S.C: O(n+m)
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        idx = 0

        for i, c in enumerate(s):
            if idx < len(spaces) and i == spaces[idx]:
                res.append(" ")
                idx += 1

            res.append(c)

        return "".join(res)
