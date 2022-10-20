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
    const result = [1]

    // calculate prefix product upto each position
    for (let index = 0; index < nums.length; index++) {
        result.push(result[index] * nums[index])
    }

    // calculate suffix product upto each position and 
    // multiply with the prefix product
    nums.push(1)
    for (let index = nums.length - 2; index >= 0; index--) {
        nums[index] = nums[index] * nums[index + 1]
        result[index] = result[index] * nums[index + 1]
    }

    result.pop()
    return result
};