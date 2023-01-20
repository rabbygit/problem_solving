class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # reverse the num strings
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0] * (len(num1) + len(num2))

        # multiply two string following basic math rule
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                result[i1 + i2] += digit
                result[i1 + i2 + 1] += (result[i1 + i2] // 10)
                result[i1 + i2] = result[i1 + i2] % 10

        result = result[::-1]
        idx = 0

        # remove leading zero
        while idx < len(result) and result[idx] == 0:
            idx += 1

        # convert int array to str array
        result = map(str, result[idx:])

        # join and return
        return "".join(result)