class Solution:
    # T.C: O(n+m) and S.C: O(1)
    def isMatched(self, char1: str, char2: str) -> bool:
        if char1 == char2:
            return True
        if chr((ord(char1) - 97 + 1) % 26 + 97) == char2:
            return True

        return False

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False

        j = 0
        k = len(str2)

        for i in range(len(str1)):
            if j == k:
                return True

            if self.isMatched(str1[i], str2[j]):
                j += 1

        return j == k
