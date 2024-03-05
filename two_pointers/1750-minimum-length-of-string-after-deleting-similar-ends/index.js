/**
 * @param {string} s
 * @return {number}
 */
// T.C: O(n) 
// S.C: O(1)
const minimumLength = function (s) {
  let l = 0;
  let r = s.length - 1;

  while (l < r && s[l] === s[r]) {
    let c = s[l];
    while (l <= r && s[l] === s[r]) {
      l++;
    }

    while (l <= r && c === s[r]) {
      r--;
    }
  }

  return r - l + 1;
};
