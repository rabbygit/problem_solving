/**
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = function (s) {
  let l = 0;
  let r = s.length - 1;
  s = s.toLowerCase();

  while (l < r) {
    while (l < r && !isAlpha(s[l])) l++;
    while (l < r && !isAlpha(s[r])) r--;
    if (s[l] != s[r]) return false;
    l++;
    r--;
  }

  return true;
};

/**
 * @param {string} c
 * @return {boolean}
 */
function isAlpha(c) {
  const asciiCode = c.charCodeAt(0);
  // "a".charCodeAt(0) = 97
  // "z".charCodeAt(0) = 122
  // "0".charCodeAt(0)= 48
  // "9".charCodeAt(0)= 57
  return (
    (asciiCode >= 97 && asciiCode <= 122) ||
    (asciiCode >= 48 && asciiCode <= 57)
  );
}
