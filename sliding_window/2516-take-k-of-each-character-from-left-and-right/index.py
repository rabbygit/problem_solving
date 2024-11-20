class Solution:
    # T.C: O(n) and S.C: O(1)
    def takeCharacters(self, s: str, k: int) -> int:
        charMap = {"a": 0, "b": 0, "c": 0}
        for ch in s:
            charMap[ch] += 1

        if min(charMap.values()) < k:
            return -1

        l, n = 0, len(s)
        res = float("inf")

        for r in range(n):
            charMap[s[r]] -= 1

            while min(charMap.values()) < k:
                charMap[s[l]] += 1
                l += 1

            res = min(res, n - (r - l + 1))

        return res
