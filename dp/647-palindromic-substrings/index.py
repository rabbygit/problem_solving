class Solution:

    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            # count odd palindrome
            l = r = i
            result += self.countPalindrome(s, l, r)

            # count even palindrome
            l = i
            r = i + 1
            result += self.countPalindrome(s, l, r)

        return result

    def countPalindrome(self, s, l, r):
        count = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1

        return count