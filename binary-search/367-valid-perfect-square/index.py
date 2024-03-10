class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        squareRoot = self.findSquareRoot(num)
        return (squareRoot * squareRoot) == num

    def findSquareRoot(self, num: int) -> bool:
        l, r = 0, num + 1

        while l < r:
            m = l + (r - l) // 2
            if m * m > num:
                r = m
            else:
                l = m + 1

        return l - 1
