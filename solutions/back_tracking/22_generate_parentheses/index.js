/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/generate-parentheses/}
 * @description Given n pairs of parentheses, 
 * write a function to generate all combinations of well-formed parentheses.
 */

/**
 * @param {number} n
 * @return {string[]}
 */
const generateParenthesis = function (n) {
  const result = []

  function generate(l, r, sub_result) {
    if (!l && !r) {
      result.push(sub_result);
      return;
    }

    if (l > r) {
      return
    }

    if (l) {
      generate(l - 1, r, sub_result + '(');
      l += 1;
    }

    if (r) {
      generate(l, r - 1, sub_result + ')');
      r += 1;
    }
  }

  generate(n, n, '');

  return result;
};

console.log(generateParenthesis(3));