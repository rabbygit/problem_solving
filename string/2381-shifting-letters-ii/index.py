from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        res = [ord(c) - ord("a") for c in s]
        prefix = [0] * (len(s) + 1)
        diff = 0

        for start, end, dir in shifts:
            prefix[end + 1] += 1 if dir == 1 else -1
            prefix[start] -= 1 if dir == 1 else -1

        for i in range(len(prefix) - 1, -1, -1):
            diff += prefix[i]
            res[i - 1] = (diff + res[i - 1] + 26) % 26

        s = [chr(ord("a") + n) for n in res]
        return "".join(s)
