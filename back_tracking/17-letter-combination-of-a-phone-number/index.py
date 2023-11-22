class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def generateCombination(i, sub_result):
            if len(sub_result) == len(digits):
                result.append(sub_result)
                return

            letters = letter_map[digits[i]]
            for char in letters:
                generateCombination(i + 1, sub_result + char)

        if digits: generateCombination(0, '')

        return result