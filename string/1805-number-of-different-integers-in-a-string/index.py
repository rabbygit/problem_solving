class Solution:

    def numDifferentIntegers(self, word: str) -> int:
        intMap = {}
        i = 0

        while i < len(word):
            if not word[i].isdigit():
                i += 1
                continue

            num = 0
            while i < len(word) and word[i].isdigit():
                num = num * 10 + int(word[i])
                i += 1

            intMap[num] = True
            i += 1

        return len(intMap)