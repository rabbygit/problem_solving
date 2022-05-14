/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/}
 * @description Given a 1-indexed array of integers numbers that is already sorted 
 * in non-decreasing order, find two numbers such that they add up to a specific target number.
 */


/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
const twoSum = function (numbers, target) {
    let left = 0
    let right = numbers.length - 1

    while (left < right) {
        // if sum is greater than target than decerease right pointer since we won't find
        // soulton in right anymore
        if (numbers[left] + numbers[right] > target) {
            right--
        } else if (numbers[left] + numbers[right] < target) {
            left++
        } else {
            return [left + 1, right + 1]
        }
    }
};