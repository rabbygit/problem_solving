/**
 * [Problem ref]{@link https://leetcode.com/problems/product-of-array-except-self/}
 * @description Given an integer array nums, return an array answer
 * such that answer[i] is equal to the product of all the elements of nums except nums[i].
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 * You must write an algorithm that runs in O(n) time and without using the division operation.
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
const productExceptSelf = function (nums) {
  const res = new Array(nums.length).fill(1);
  let prefixProd = 1;
  let suffixProd = 1;

  for (let i = 0; i < nums.length; i++) {
    res[i] = prefixProd;
    prefixProd *= nums[i];
  }

  for (let i = nums.length - 1; i > -1; i--) {
    res[i] *= suffixProd;
    suffixProd *= nums[i];
  }

  return res;
};
