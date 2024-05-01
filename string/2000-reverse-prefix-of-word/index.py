class Solution:
    # T.C and S.C: O(n)
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ""

        for idx, c in enumerate(word):
            res = c + res
            if c == ch:
                res += word[idx + 1 :]
                return res

        return word
