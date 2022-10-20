/**
 * 
 
 * [Problem ref]{@link  https://leetcode.com/problems/remove-duplicates-from-sorted-array/}
 * @param {number[]} nums
 * @return {number}
 */
// solution: 1
// Runtime: 0(n2)
const removeDuplicates = function (nums) {
    let k = 0;
    for (let i = 0; i < nums.length; i++) {
        k++;
        nums[k - 1] = nums[i];

        for (let j = i + 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                break;
            } else {
                i++
            }
        }
    }
    return k;
};

// solution: 2
// Runtime: 0(n)
/**
 * @param {number[]} nums
 * @return {number}
 */
const removeDuplicates = function (nums) {
    let n = nums.length
    if (!n) return 0;

    let k = 1
    let j = 1
    let replace_idx = 1

    for (let i = 0; i < n - 1; i++) {
        if (nums[i] != nums[j]) {
            k++
            nums[replace_idx] = nums[j]
            replace_idx++
        }

        j++
    }

    return k;
};