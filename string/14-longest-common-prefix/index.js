/**
 * [Problem ref]{@link https://leetcode.com/problems/longest-common-prefix/}
 * @description Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 */

/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = function (strs) {
  const res = strs[0];

  for (let i = 0; i < res.length; i++) {
    for (let j = 1; j < strs.length; j++) {
      if (i >= strs[j].length || res[i] !== strs[j][i]) {
        return res.substring(0, i);
      }
    }
  }

  return res;
};
