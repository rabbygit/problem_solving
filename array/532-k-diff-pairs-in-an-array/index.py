class Solution:

    def findPairs(self, nums: List[int], k: int) -> int:
        numbers = set()
        result = set()

        for n in nums:
            if (n + k) in numbers:
                result.add(n)
            if (n - k) in numbers:
                result.add(n - k)

            numbers.add(n)

        return len(result)