class Solution:
    def mySqrt(self, x: int) -> int:
        return self.findSqrt(x , 1 , x)

    def findSqrt(self , n , left , right):
        if left > right:
            return right

        # find mid by integer division
        mid = (left + right) // 2

        if mid * mid > n:
            return self.findSqrt(n, left , mid - 1)
        elif mid * mid < n:
            return self.findSqrt(n , mid + 1 , right)
        else:
            return mid
