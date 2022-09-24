/**
 * [Problem ref]{@link https://leetcode.com/problems/longest-repeating-character-replacement/}
 * @description You are given a string s and an integer k. You can choose any character of the string and
 *  change it to any other uppercase English character. You can perform this operation at most k times.
 * Return the length of the longest substring containing the same letter you can get after performing the above operations.
 */

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
const characterReplacement = function (s, k) {
  const count = {};
  let result = 1;
  let left = 0;
  let maxCount = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    count[char] = (count[char] === undefined ? 0 : count[char]) + 1;

    maxCount = Math.max(maxCount, count[char]);

    if (right - left + 1 - maxCount > k) {
      count[s[left]]--;
      left++;
    }

    result = Math.max(result, right - left + 1);
  }

  return result;
};
