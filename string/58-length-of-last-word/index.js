/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLastWord = function (s) {
  let len = 0;
  for (let i = s.length - 1; i > -1; i--) {
    if (len && s[i] === " ") {
      return len;
    } else if (s[i] !== " ") {
      len++;
    }
  }
  return len;
};
