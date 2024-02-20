class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x < n:
            x *= 2
        return x == n


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        # largest 2^n value
        return n > 0 and ((2**30) % n == 0)


class Solution3:
    def isPowerOfTwo(self, n: int) -> bool:
        # largest 2^n value
        return n > 0 and ((1 << 30) % n == 0)


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n = 8 = 1000 -> (n-1) = 7 = 0111 (it works if there is only 1 bit(1) in the number)
        # so, n = 1000 and (n - 1) = 0111. n & (n-1) = 0
        return n > 0 and (n & (n - 1) == 0)
