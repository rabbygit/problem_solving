/**
 * [Problem ref]{@link  https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/}
 * @description Given an array nums of n integers where nums[i] is in the range [1, n], 
 * return an array of all the integers in the range [1, n] that do not appear in nums.
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
const findDisappearedNumbers = function (nums) {
    const n = nums.length
    // construct result array with [1,n] values
    const result = Array.from({ length: n }, (_, index) => index + 1)

    for (let index = 0; index < n; index++) {
        let val = nums[index]
        // if this value found in result array,that means it's not missing and mark it
        if (result[val - 1] == val) {
            result[val-1] = false
        }
    }
   
    // filter found elements
    return result.filter(element => element)
};