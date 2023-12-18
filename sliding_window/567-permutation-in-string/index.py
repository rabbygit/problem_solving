# T.C: (26 * n)
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


# T.C: (n)
class Solution1:

    def index(self, char):
        return ord(char) - ord('a')

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26
        l = matches = 0

        for i in range(len(s1)):
            s1Count[self.index(s1[i])] += 1
            s2Count[self.index(s2[i])] += 1

        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = self.index(s2[r])
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = self.index(s2[l])
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1

        return matches == 26
