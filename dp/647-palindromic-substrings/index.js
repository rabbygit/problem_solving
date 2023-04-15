/**
 * @param {string} s
 * @return {number}
 */
const countSubstrings = function (s) {
  let result = 0;

  for (let index = 0; index < s.length; index++) {
    // count odd palindrome
    let l = index;
    let r = index;
    result += countPalindrome(s, l, r);

    // count even palindrome
    l = index;
    r = index + 1;
    result += countPalindrome(s, l, r);
  }

  return result;
};

function countPalindrome(s, l, r) {
  let count = 0;

  while (l >= 0 && r < s.length && s[l] === s[r]) {
    l -= 1;
    r += 1;
    count++;
  }

  return count;
}
