/**
 * [Problem ref]{@link  https://leetcode.com/problems/search-insert-position/}
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const searchInsert = function (nums, target) {
    return search(nums, 0, nums.length - 1, target)
};

const search = function (nums, left, right, target) {
    if (right >= left) {
        let mid = left + Math.floor((right - left) / 2);

        if (nums[mid] == target) {
            return mid;
        }

        if (target < nums[mid]) {
            return search(nums, left, mid - 1, target);
        }

        return search(nums, mid + 1, right, target);
    }

    return left;
}