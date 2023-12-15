from typing import List


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_s = [0] * 26
        freq_p = [0] * 26
        l, res = 0, []

        for c in p:
            freq_p[ord(c) - 97] += 1

        for r in range(len(s)):
            c = s[r]
            freq_s[ord(c) - 97] += 1
            if r - l + 1 == len(p) and freq_s == freq_p:
                res.append(l)

            if r - l + 1 >= len(p):
                freq_s[ord(s[l]) - 97] -= 1
                l += 1
 
        return res