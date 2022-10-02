class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        charSet1 = {}
        charSet2 = {}

        if (len(s2) < len(s1)):
            return False

        for i in range(len(s1)):
            charSet1[s1[i]] = charSet1.get(s1[i], 0) + 1
            charSet2[s2[i]] = charSet2.get(s2[i], 0) + 1

        for right in range(len(s1) - 1, len(s2)):
            if isEqual(charSet1, charSet2):
                return True

            charSet2[s2[left]] -= 1
            left += 1

            if right + 1 < len(s2):
                charSet2[s2[right + 1]] = charSet2.get(s2[right + 1], 0) + 1

        return False


def isEqual(hash1, hash2):
    for key in hash1:
        if key not in hash2 or hash1[key] != hash2[key]:
            return False

    return True