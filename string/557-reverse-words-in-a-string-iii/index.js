/**
 * @param {string} s
 * @return {string}
 */
const reverseWords = function (s) {
  let res = "";
  let reversed = "";

  for (let i = 0; i < s.length; i++) {
    if (s[i] === " ") {
      res += reversed + " ";
      reversed = "";
    } else {
      reversed = s[i] + reversed;
    }
  }

  return res + reversed;
};
