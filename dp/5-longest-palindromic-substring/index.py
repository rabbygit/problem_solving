class Solution:

    def longestPalindrome(self, s: str) -> str:
        start = end = 0

        for i in range(len(s)):
            # get longest odd palindrome
            l = r = i
            ps, pe = self.subPalindrome(s, l, r)
            if pe - ps > end - start:
                start, end = ps, pe

            # get longest even palindrome
            l = i
            r = i + 1
            ps, pe = self.subPalindrome(s, l, r)
            if pe - ps > end - start:
                start, end = ps, pe

        return s[start:end + 1]

    def subPalindrome(self, s, l, r):
        start = end = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            start, end = l, r
            l -= 1
            r += 1

        return (start, end)