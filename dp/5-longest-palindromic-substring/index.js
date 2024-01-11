/**
 * @param {string} s
 * @return {string}
 */
const longestPalindrome = function (s) {
  let start = 0;
  let end = 0;

  for (let i = 0; i < s.length; i++) {
    // odd palindrome
    let left = i;
    let right = i;
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      if (right - left > end - start) {
        start = left;
        end = right;
      }

      left--;
      right++;
    }

    // even palindrome
    left = i;
    right = i + 1;
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      if (right - left > end - start) {
        start = left;
        end = right;
      }

      left--;
      right++;
    }
  }

  return s.slice(start, end + 1);
};
