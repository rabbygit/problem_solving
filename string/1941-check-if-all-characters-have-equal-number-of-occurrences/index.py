class Solution:

    def areOccurrencesEqual(self, s: str) -> bool:
        charOccur = [0] * 26

        for char in s:
            charOccur[ord(char) - 97] += 1

        compareValue = charOccur[ord(s[0]) - 97]
        for char in s:
            if charOccur[ord(char) - 97] != compareValue:
                return False

        return True