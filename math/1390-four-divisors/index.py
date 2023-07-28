import math
from typing import List


class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0

        for n in nums:
            result += self.findDivisorsSum(n)

        return result

    def findDivisorsSum(self, n: int) -> int:
        divisors = set([1, n])

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
            if len(divisors) > 4:
                return 0

        return sum(divisors) if len(divisors) == 4 else 0