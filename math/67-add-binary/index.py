class Solution:

    def addBinary(self, a: str, b: str) -> str:
        result, carry = '', 0
        i, j = len(a) - 1, len(b) - 1

        while i > -1 or j > -1 or carry:
            x = 0 if i < 0 else int(a[i])
            y = 0 if j < 0 else int(b[j])
            currSum = x + y + carry

            if currSum == 3:
                result = '1' + result
                carry = 1
            elif currSum == 2:
                result = '0' + result
                carry = 1
            elif currSum == 1:
                result = '1' + result
                carry = 0
            else:
                result = '0' + result
                carry = 0

            i -= 1
            j -= 1

        return result