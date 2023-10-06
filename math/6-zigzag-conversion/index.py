class Solution:

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        res = [""] * numRows
        idx, up = 1, True

        for c in s:
            res[idx - 1] += c

            if idx == numRows:
                up = False
            elif idx == 1:
                up = True

            if up:
                idx += 1
            else:
                idx -= 1

        return "".join(res)