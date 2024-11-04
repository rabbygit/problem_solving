class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        count = 1
        prev = word[0]

        for i in range(1, len(word)):
            c = word[i]
            if prev == c and count < 9:
                count += 1
            else:
                res.append(str(count) + prev)
                count = 1
                prev = c

        res.append(str(count) + prev)

        return "".join(res)
