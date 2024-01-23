from typing import List

# T.C: 2^n * m
class Solution:

    def maxLength(self, arr: List[str]) -> int:
        self.maxLen = 0

        def backtrack(i: int, sub: str):
            if i >= len(arr): return

            tmp = sub
            sub += arr[i]
            charSet = set(sub)
            if len(sub) == len(charSet):
                self.maxLen = max(self.maxLen, len(sub))

            backtrack(i+1, sub)
            backtrack(i+1, tmp)

        backtrack(0, '')
            
        return self.maxLen