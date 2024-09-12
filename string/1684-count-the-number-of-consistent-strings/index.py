from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedCharMap = set(allowed)
        res = 0

        for word in words:
            isAllCharAppeared = True
            for c in word:
                if c not in allowedCharMap:
                    isAllCharAppeared = False
                    break
            
            if isAllCharAppeared:
                res += 1
            
        return res
            
