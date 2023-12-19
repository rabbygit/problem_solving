class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        idx = 0
        for i in range(len(t)):
            if idx == len(s):
                return True
            elif s[idx] == t[i]:
                idx += 1

        return idx == len(s)
