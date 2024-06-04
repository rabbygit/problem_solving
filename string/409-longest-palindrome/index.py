import collections


class Solution:
    # T.C and S.C: O(n)
    def longestPalindrome(self, s: str) -> int:
        charMap = collections.defaultdict(int)
        res = 0

        for c in s:
            charMap[c] += 1
            if charMap[c] % 2 == 0:
                res += 2

        for v in charMap.values():
            if v % 2:
                res += 1
                break

        return res


class Solution1:
    # T.C and S.C: O(n)
    def longestPalindrome(self, s: str) -> int:
        visited = set()
        res = 0

        for c in s:
             # it means char has even length
            if c in visited:
                visited.remove(c)
                res += 2
            else:
                # it means char has odd length
                visited.add(c)

        return res + 1 if visited else res
