/**
 * 
 
 * [Problem ref]{@link https://leetcode.com/problems/merge-sorted-array/}
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
const merge = function (nums1, m, nums2, n) {
    let index = m + n - 1;
    m -= 1;
    n -= 1;
    while (index >= 0) {
        if (m >= 0) {
            if (nums2[n] >= nums1[m]) {
                nums1[index] = nums2[n];
                n--;
            } else {
                nums1[index] = nums1[m];
                m--;
            }
        } else {
            nums1[index] = nums2[n];
            n--;
        }
        index--;
    }

    if (!n && nums1[0] > nums2[0]) {
        nums1[0] = nums2[0];
    }

    return nums1
};