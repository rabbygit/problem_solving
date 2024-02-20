class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # skipping left char
                if self.isValidPart(s[l + 1 : r + 1]):
                    return True
                if self.isValidPart(s[l:r]):
                    return True
                return False

            l += 1
            r -= 1

        return True

    def isValidPart(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
