from math import sqrt


class Solution:

    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i

        for i in range(int(sqrt(n)), 0, -1):
            if i * i != n and n % i == 0:
                k -= 1
                if k == 0:
                    return n // i

        return -1
