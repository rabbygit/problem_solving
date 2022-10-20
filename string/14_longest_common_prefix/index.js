/**
 * [Problem ref]{@link https://leetcode.com/problems/longest-common-prefix/}
 * @description Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 */


/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = function(strs) {
    let result = ''

    for (let index = 0; index < strs[0].length; index++) {
        result += strs[0][index] // add character assuming upto this character is common
        for (let j = 1; j < strs.length; j++) {
            // if not matched then remove last added char
            if (index >= strs[j].length || strs[j][index] !== strs[0][index]) {
               result = result.slice(0,-1) 
               return result
            }
        }
    }


    return result
};