/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/valid-parentheses/}
 * @description Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
 * determine if the input string is valid.
 */

/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = function (s) {
    const stack = []
    const parentheses_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for (let index = 0; index < s.length; index++) {
        const parentheses = s[index];
        // if it is in the map. that means it's the openning bracket
        // else it's the closing bracket and compare with the last element of stack
        // since the last stack's bracket is the last openning bracket we put as closing bracket, so it should be equal
        if (parentheses_map[parentheses]) {
            stack.push(parentheses_map[parentheses])
        }else{
            if (parentheses !== stack.pop()) {
                return false
            }
        }
    }

    return stack.length === 0
};