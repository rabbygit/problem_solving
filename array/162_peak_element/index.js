/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/find-peak-element/}
 * @description A peak element is an element that is strictly greater than its neighbors.
 * Given an integer array nums, find a peak element, and return its index. 
 * If the array contains multiple peaks, return the index to any of the peaks.
 * You may imagine that nums[-1] = nums[n] = -∞.
 * You must write an algorithm that runs in O(log n) time.
 */


/**
 * @param {number[]} nums
 * @return {number}
 */
const findPeakElement = function (nums) {
    let left = 0
    let right = nums.length - 1

    while (left < right) {
        let middle = parseInt((left + right) / 2)

        if (nums[middle] > nums[middle + 1]) {
            right = middle
        } else {
            left = middle + 1
        }
    }

    return left
};