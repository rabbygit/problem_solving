/**
 * [Problem ref]{@link https://leetcode.com/problems/longest-substring-without-repeating-characters/}
 * @description Given a string s, find the length of the longest substring without repeating characters.
 */

/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = function (s) {
  let result = 0;
  let left = 0;
  const charSet = {};

  for (let right = 0; right < s.length; right++) {
    while (charSet[s[right]]) {
      delete charSet[s[left]];
      left++;
    }

    charSet[s[right]] = true;
    result = Math.max(result, right - left + 1);
  }

  return result;
};
