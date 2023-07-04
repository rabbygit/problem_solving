class Solution:

    def firstUniqChar(self, s: str) -> int:
        charMap = {}

        for char in s:
            if char not in charMap:
                charMap[char] = 1
            else:
                charMap[char] += 1

        for i in range(len(s)):
            if charMap[s[i]] == 1:
                return i

        return -1