from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numMap = {}
        n = len(grid)
        repeatedNum = sumWithoutRepeatedNum = 0

        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                if num in numMap:
                    repeatedNum = num
                    numMap[num] = 2
                else: 
                    numMap[num] = 1
                    sumWithoutRepeatedNum += num

        lastDigit = n * n
        expectedSum = (1 + lastDigit) * (lastDigit / 2)
        missing = expectedSum - sumWithoutRepeatedNum

        return [repeatedNum, int(missing)]