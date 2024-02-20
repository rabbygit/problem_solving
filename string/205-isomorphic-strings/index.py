class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for i, c in enumerate(s):
            if c not in sMap and t[i] not in tMap:
                sMap[c] = t[i]
                tMap[t[i]] = c
            elif (c in sMap and sMap[c] != t[i]) or (t[i] in tMap and tMap[t[i]] != c):
                return False

        return True
