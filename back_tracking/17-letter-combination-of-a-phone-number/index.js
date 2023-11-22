/**
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
  const result = [];
  const letter_map = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
  };

  function generateCombination(i, sub_result) {
    if (sub_result.length === digits.length) {
      result.push(sub_result);
      return;
    }

    let letters = letter_map[digits[i]];
    for (const char of letters) {
      generateCombination(i + 1, sub_result + char);
    }
  }

  if (digits) generateCombination(0, "");
  return result;
};
