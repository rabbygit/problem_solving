/**
 * [Problem ref]{@link https://leetcode.com/problems/valid-parentheses/}
 * @description Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 * determine if the input string is valid.
 */

/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = function (s) {
  const stack = [];
  const parentheses_map = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    // if it is in the map. that means it's the openning bracket
    // else it's the closing bracket and compare with the last element of stack
    // since the last stack's bracket is the last openning bracket we put as closing bracket, so it should be equal
    if (parentheses_map[c]) {
      stack.push(parentheses_map[c]);
      continue;
    }

    if (stack.length === 0 || c !== stack.pop()) {
      return false;
    }
  }

  return stack.length === 0;
};
