/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/reverse-words-in-a-string/}
 * @description Given an input string s, reverse the order of the words.
 * A word is defined as a sequence of non-space characters. 
 * The words in s will be separated by at least one space.
 */

/**
 * @param {string} s
 * @return {string}
 */
const reverseWords = function (s) {
    let temp = ''
    let stack = []

    // push word in stack
    for (let index = 0; index < s.length; index++) {
        if (s[index] == ' ' && temp.length) {
            stack.push(temp)
            temp = ''
        }

        if (s[index] != ' ') {
            temp += s[index]
        }
    }

    // any word left?
    if (temp.length) {
        stack.push(temp)
        temp = ''
    }

    // push the last word from stack
    temp = stack[stack.length-1]

    // add other words
    for (let index = stack.length - 2; index >= 0; index--) {
        temp += ' ' + stack[index]
    }

    return temp
};