import math


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        windowHash, countHash = {}, {}
        have = 0
        left = 0
        result = [-1, -1]
        resultLength = math.inf

        for c in t:
            countHash[c] = 1 + countHash.get(c, 0)

        need = len(countHash)

        for right in range(len(s)):
            char = s[right]
            windowHash[char] = 1 + windowHash.get(char, 0)

            if char in countHash and windowHash[char] == countHash[char]:
                have += 1

            while have == need:
                if (right - left + 1) < resultLength:
                    resultLength = right - left + 1
                    result = [left, right]

                # pop the left most char from window
                l_char = s[left]
                windowHash[l_char] -= 1
                if l_char in countHash and windowHash[l_char] < countHash[
                        l_char]:
                    have -= 1

                # increment left pointer
                left += 1

        if resultLength == math.inf:
            return ""
        else:
            left, right = result
            return s[left:right + 1]
