import collections


class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charMap = collections.defaultdict(int)

        for c in magazine:
            charMap[c] += 1

        for c in ransomNote:
            if c not in charMap or charMap[c] < 1:
                return False

            charMap[c] -= 1

        return True