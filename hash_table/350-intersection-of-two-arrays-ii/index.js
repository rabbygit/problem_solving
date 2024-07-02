/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
const intersect = function (nums1, nums2) {
  if (nums1.length > nums2.length) {
    return intersect(nums2, nums1);
  }

  const result = [];
  const numsMap = {};

  // keep number occurance map
  for (const n of nums1) {
    numsMap[n] = numsMap[n] ? numsMap[n] + 1 : 1;
  }

  // find the common numbers
  for (const n of nums2) {
    if (numsMap[n] > 0) {
      result.push(n);
      numsMap[n] = numsMap[n] - 1;
    }
  }

  return result;
};
