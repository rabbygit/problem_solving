/**
 * @param {string} s
 * @return {boolean}
 */
var areOccurrencesEqual = function (s) {
  const charOccur = new Array(26).fill(0);

  for (const char of s) {
    charOccur[char.charCodeAt(0) - 97]++;
  }

  const compareValue = charOccur[s[0].charCodeAt(0) - 97];

  for (const char of s) {
    if (charOccur[char.charCodeAt(0) - 97] !== compareValue) {
      return false;
    }
  }

  return true;
};
