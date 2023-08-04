class Solution:

    def countVowelSubstrings(self, word: str) -> int:
        vowels = 'aeiou'

        result = 0
        start = 0
        vowel_idx = {}

        for idx, c in enumerate(word):
            if c in vowels:
                if not vowel_idx:
                    start = idx
                vowel_idx[c] = idx
                if len(vowel_idx) == 5:
                    result += min(vowel_idx.values()) - start + 1
            else:
                vowel_idx.clear()

        return result