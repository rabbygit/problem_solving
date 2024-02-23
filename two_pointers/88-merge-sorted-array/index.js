/**
 *
 * [Problem ref]{@link https://leetcode.com/problems/merge-sorted-array/}
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
// time complexity: O(m + n)
// space complexity: O(1)
const merge = function (nums1, m, nums2, n) {
  let index = m + n - 1;
  m -= 1;
  n -= 1;

  // merge from the end since "the last n elements are set to 0"
  // nums1 = [1,2,3,0,0,0], nums2 = [2,5,6]
  while (m >= 0 && n >= 0) {
    if (nums2[n] > nums1[m]) {
      nums1[index] = nums2[n];
      n--;
    } else {
      nums1[index] = nums1[m];
      m--;
    }
    index--;
  }

  // merge the remaining form nums2
  if (n >= 0) {
    nums1[index] = nums2[n];
    n--;
    index--;
  }
};
