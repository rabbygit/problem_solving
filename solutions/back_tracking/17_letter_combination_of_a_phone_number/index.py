class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
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

        def generateCombination(sub_result,letter_index):
            if len(sub_result) == n:
                result.append(sub_result)
                return
            
            letters = letter_map[digits[letter_index]]
            for letter in letters:
                generateCombination(sub_result + letter , letter_index + 1)

        
        if not n:
            return result
        
        generateCombination('',0)

        return result