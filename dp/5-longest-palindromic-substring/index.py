class Solution:

    def longestPalindrome(self, s: str) -> str:
        result = ''

        for i in range(len(s)):
            # get longest odd palindrome
            l = r = i
            subLongPalindrome = self.subPalindrome(s, l, r)
            if len(subLongPalindrome) > len(result):
                result = subLongPalindrome

            # get longest even palindrome
            l = i
            r = i + 1
            subLongPalindrome = self.subPalindrome(s, l, r)
            if len(subLongPalindrome) > len(result):
                result = subLongPalindrome

        return result

    def subPalindrome(self, s, l, r):
        longestPalindrome = ''

        while l >= 0 and r < len(s) and s[l] == s[r]:
            longestPalindrome = s[l:r + 1]
            l -= 1
            r += 1

        return longestPalindrome