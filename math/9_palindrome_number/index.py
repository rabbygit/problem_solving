class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        result = 0
        digit = 0
        n = x

        while n:
            digit = n % 10
            result = (result*10) + digit
            n = int(n/10)

        return x == result
