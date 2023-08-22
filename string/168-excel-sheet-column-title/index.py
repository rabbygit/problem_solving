class Solution:

    def convertToTitle(self, columnNumber):
        output = ''

        while columnNumber > 0:
            columnNumber -= 1
            output = chr(ord('A') + columnNumber % 26) + output
            columnNumber = columnNumber // 26

        return output