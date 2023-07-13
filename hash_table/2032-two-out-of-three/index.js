/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @return {number[]}
 */
const twoOutOfThree = function (nums1, nums2, nums3) {
  const map1 = new Map(nums1.map((n) => [n, true]));
  const map2 = new Map();
  const res = new Map();

  for (const n of nums2) {
    map2.set(n, true);
    if (map1.has(n)) res.set(n, true);
  }

  for (const n of nums3) {
    if (map1.has(n) || map2.has(n)) res.set(n, true);
  }

  return Array.from(res.keys());
};
