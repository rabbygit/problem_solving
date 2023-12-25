class Solution:

    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        remainingDays = n % 7
        firstWeek = 28
        lastWeek = 28 + 7 * (weeks - 1)
        # formula: 1 + 2 + 3 + 4 + 5 + 6 = (1st + last) * (n/2) = (1+6) * 6 / 2
        result = int((firstWeek + lastWeek) * (weeks / 2))

        start = weeks + 1
        for i in range(remainingDays):
            result += start + i

        return result
