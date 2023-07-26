import math


class Solution:

    def countPrimes(self, n: int) -> int:
        if n < 2: return 0

        composites = [False] * n
        result = 0

        for i in range(2, int(math.sqrt(n))):
            if composites[i] == False:
                for j in range(i * i, n, i):
                    composites[j] = True

        for i in range(n):
            if composites[i] == False:
                result += 1

        return result