/**
 * [Problem ref]{@link  https://leetcode.com/problems/find-all-duplicates-in-an-array/}
 * @description Given an integer array nums of length n where all the integers of nums are in the range [1, n] and 
 * each integer appears once or twice, return an array of all the integers that appears twice.
 * You must write an algorithm that runs in O(n) time and uses only constant extra space
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
const findDuplicates = function (nums) {
    const result = []

    for (let index = 0; index < nums.length; index++) {
        let pos = Math.abs(nums[index]) - 1
        if (nums[pos] < 0) {
            result.push(pos + 1)
        }
        nums[pos] = -nums[pos]
    }

    return result
};