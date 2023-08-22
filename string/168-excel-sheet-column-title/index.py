class Solution:

    def convertToTitle(self, columnNumber):
        output = ''

        while columnNumber > 0:
            charNumber = columnNumber - 1
            output = chr(ord('A') + charNumber % 26) + output
            columnNumber = charNumber // 26

        return output