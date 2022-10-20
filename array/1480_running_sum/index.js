/**
 * [Problem ref]{@link  https://leetcode.com/problems/running-sum-of-1d-array/}
 * @description Given an array nums. 
 * We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
const runningSum = function(nums) {
    for (let index = 1; index < nums.length; index++) {
        nums[index] = nums[index-1] + nums[index]
    }

    return nums
};