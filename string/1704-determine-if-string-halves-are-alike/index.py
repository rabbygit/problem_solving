class Solution:

    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        return self.countVowels(s[:mid]) == self.countVowels(s[mid:])

    def countVowels(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count = 0

        for c in s:
            if c in vowels:
                count += 1

        return count
