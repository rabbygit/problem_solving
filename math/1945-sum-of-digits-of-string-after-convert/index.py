class Solution:
    # T.C: O(n) and S.C: O(1)
    def getLucky(self, s: str, k: int) -> int:
        total = 0
        for c in s:
            position = str(ord(c) % 96)
            for d in position:
                total += int(d)

        k -= 1
        while k:
            total = self.sumOfDigits(total)
            k -= 1

        return total

    def sumOfDigits(self, num: int) -> int:
        tmpSum = 0
        while num:
            digit = num % 10
            num = num // 10
            tmpSum += digit
        return tmpSum
