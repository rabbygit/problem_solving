/**
 * Definition for isBadVersion()
 *
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
const solution = function (isBadVersion) {
  /**
   * @param {integer} n Total versions
   * @return {integer} The first bad version
   */
  return function (n) {
    let l = 1;
    let r = n;
    let mid = 1;

    while (l <= r) {
      mid = l + parseInt((r - l) / 2);
      if (isBadVersion(mid) && !isBadVersion(mid - 1)) {
        return mid;
      } else if (isBadVersion(mid) && isBadVersion(mid - 1)) {
        r = mid - 1;
      } else {
        l = mid + 1;
      }
    }

    return mid;
  };
};
