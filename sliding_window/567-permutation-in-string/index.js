/**
 * [Problem ref]{@link https://leetcode.com/problems/permutation-in-string/}
 * @description Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
 * In other words, return true if one of s1's permutations is the substring of s2.
 */

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
const checkInclusion = function (s1, s2) {
  let left = 0;
  const charSetS1 = {};
  const charSetS2 = {};

  if (s2.length < s1.length) return false;

  for (let index = 0; index < s1.length; index++) {
    const char1 = s1[index];
    const char2 = s2[index];

    if (charSetS1[char1] === undefined) {
      charSetS1[char1] = 1;
    } else {
      charSetS1[char1] = charSetS1[char1] + 1;
    }

    if (charSetS2[char2] === undefined) {
      charSetS2[char2] = 1;
    } else {
      charSetS2[char2] = charSetS2[char2] + 1;
    }
  }

  for (let right = s1.length - 1; right < s2.length; right++) {
    if (isEqual(charSetS1, charSetS2)) return true;

    charSetS2[s2[left]]--;
    const char2 = s2[right + 1];
    if (charSetS2[char2] === undefined) {
      charSetS2[char2] = 1;
    } else {
      charSetS2[char2] = charSetS2[char2] + 1;
    }
    left++;
  }

  return false;
};

function isEqual(hash1, hash2) {
  for (const key of Object.keys(hash1)) {
    if (hash2[key] === undefined || hash2[key] !== hash1[key]) {
      return false;
    }
  }

  return true;
}
