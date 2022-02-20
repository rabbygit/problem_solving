/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/single-number/}
 * @description Given a non-empty array of integers nums, every element appears twice except for one. 
 * Find that single one.You must implement a solution with a linear runtime complexity and 
 * use only constant extra space.
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
const singleNumber = function(nums) {
    let result = 0
    for (let index = 0; index < nums.length; index++) {
        // xor operation returns 0 if both bits are same and 1 for different bits
        // so, if we xor two same number it will return 0 and after that xor with unique number
        // it will give the unique number
        // Ex: [2,2,1] 010 ^ 010 = 000 ^ 001 = 001 
        result = result ^ nums[index]
    }

    return result
};