/**
 * Problem ref: 26. https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
 const removeDuplicates = function(nums) {
    let k = 0; 
    for (let i = 0; i < nums.length; i++) {
        k++;
        nums[k-1] = nums[i];

        for (let j = i+1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                break;
            } else {
                i++
            }
        }
    }
    return k;
};