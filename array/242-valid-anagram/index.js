/**
 * [Problem ref]{@link https://leetcode.com/problems/valid-anagram/}
 * @description Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 * typically using all the original letters exactly once.
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  const s_map = new Map();

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    const occurrence = s_map.get(s[i]);
    if (occurrence === undefined) {
      s_map.set(char, 1);
    } else {
      s_map.set(char, occurrence + 1);
    }
  }

  for (let i = 0; i < t.length; i++) {
    const occurrence = s_map.get(t[i]);
    if (occurrence === undefined || occurrence === 0) {
      return false;
    }

    s_map.set(t[i], occurrence - 1);
  }

  return true;
};
