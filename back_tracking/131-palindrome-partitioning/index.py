class Solution:

    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(i, partion):
            if i >= len(s):
                result.append(partion.copy())
                return

            for index in range(i, len(s)):
                if self.isPalindrome(s, i, index):
                    partion.append(s[i:index + 1])
                    backtrack(index + 1, partion)
                    partion.pop()

        backtrack(0, [])

        return result

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True