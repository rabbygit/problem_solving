class Solution:

    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.calculateSum(n)

            if n == 1:
                return True

        return False

    def calculateSum(self, n: int) -> int:
        sum = 0

        while n:
            digit = n % 10
            sum += digit**2
            n = n // 10

        return sum
