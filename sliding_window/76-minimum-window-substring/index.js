/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/minimum-window-substring/description/}
 * @description Given two strings s and t of lengths m and n respectively,
 * return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
 * If there is no such substring, return the empty string "".
 * The testcases will be generated such that the answer is unique.
 * A substring is a contiguous sequence of characters within the string
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
const minWindow = (s, t) => {
  if (t.length > s.length) return "";

  const windowHash = {};
  const countHash = {};
  let result = [-1, -1];
  let left = 0;
  let have = 0;
  let resultLength = Infinity;

  for (const char of t) {
    if (countHash[char] === undefined) {
      countHash[char] = 1;
    } else {
      countHash[char]++;
    }
  }

  const need = Object.keys(countHash).length;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    if (windowHash[char] === undefined) {
      windowHash[char] = 1;
    } else {
      windowHash[char]++;
    }

    if (countHash[char] !== undefined && countHash[char] === windowHash[char]) {
      have++;
    }

    while (have === need) {
      if (right - left + 1 < resultLength) {
        result = [left, right];
        resultLength = right - left + 1;
      }

      const lChar = s[left];
      windowHash[lChar]--;
      left++;
      if (countHash[lChar] && windowHash[lChar] < countHash[lChar]) {
        have--;
      }
    }
  }

  if (resultLength === Infinity) {
    return "";
  } else {
    return s.slice(result[0], result[1] + 1);
  }
};