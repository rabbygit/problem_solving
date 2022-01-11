/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/letter-combinations-of-a-phone-number/}
 * @description Given a string containing digits from 2-9 inclusive,
 * return all possible letter combinations that the number could represent. 
 * Return the answer in any order.
 */

/**
 * @param {string} digits
 * @return {string[]}
 */
const letterCombinations = function (digits) {
    const n = digits.length
    const result = []
    const letter_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    function generateCombination(sub_result, digit_index) {
        if (sub_result.length === n) {
            result.push(sub_result)
            return
        }

        let letters = letter_map[digits[digit_index]];
        for (let index = 0; index < letters.length; index++) {
            const letter = letters[index];
            generateCombination(sub_result + letter, digit_index + 1)
        }
    }

    if (!n) return result

    generateCombination('', 0)
    return result
};