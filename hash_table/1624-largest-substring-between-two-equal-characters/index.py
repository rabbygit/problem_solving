class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        charMap = {}
        maxLen = -1

        for idx, c in enumerate(s):
            if c in charMap:
                maxLen = max(maxLen, idx - charMap[c] - 1)
            else:
                charMap[c] = idx

        return maxLen