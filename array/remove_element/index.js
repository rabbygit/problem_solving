/**
 * 
 
 * [Problem ref]{@link  https://leetcode.com/problems/remove-element/}
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
const removeElement = function (nums, val) {
    let k = 0;
    for (let index = 0; index < nums.length; index++) {
        if (nums[index] != val) {
            nums[k] = nums[index]
            k++
        }
    }

    return k;
};