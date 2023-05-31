/**
 * @param {string} s
 * @return {string}
 */
const longestPalindrome = function (s) {
  let res = "";
  let resLength = 0;

  for (let i = 0; i < s.length; i++) {
    // odd palindrome
    let left = i;
    let right = i;
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      if (right - left + 1 > resLength) {
        res = s.substring(left, right + 1);
        resLength = right - left + 1;
      }

      left--;
      right++;
    }

    // even palindrome
    left = i;
    right = i + 1;
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      if (right - left + 1 > resLength) {
        res = s.substring(left, right + 1);
        resLength = right - left + 1;
      }

      left--;
      right++;
    }
  }

  return res;
};
