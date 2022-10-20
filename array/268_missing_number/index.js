/**
 * [Problem ref]{@link  https://leetcode.com/problems/missing-number/}
 * @description Given an array nums containing n distinct numbers in the range [0, n], 
 * return the only number in the range that is missing from the array.
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
const missingNumber = function (nums) {
    const n = nums.length
    // summation of sequence numbers ex: 1+2+3+..
    const total_sum = (n * (n + 1)) / 2
    let total = 0

    // loop thhrugh every number and calculate total sum
    for (let index = 0; index < n; index++) {
        total += nums[index]
    }

    // subtraction result is the missing number
    return total_sum - total
};