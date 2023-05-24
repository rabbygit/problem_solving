/**
 *
 * [Problem ref]{@link  https://leetcode.com/problems/two-sum/}
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = function (nums, target) {
  const numHash = {}; // number -> index

  for (let index = 0; index < nums.length; index++) {
    const value = target - nums[index];

    if (numHash[value] !== undefined) {
      return [numHash[value], index];
    } else {
      numHash[nums[index]] = index;
    }
  }

  return [];
};
