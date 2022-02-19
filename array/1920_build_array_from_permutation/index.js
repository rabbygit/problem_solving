/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/build-array-from-permutation/}
 * @description Given a zero-based permutation nums (0-indexed), 
 * build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
 * A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
const buildArray = function (nums) {
    const n = nums.length

    for (let index = 0; index < n; index++) {
        // this is done to keep both old and new value together. 
        // going by the example of [5,0,1,2,3,4]
        // after this nums[0] will be 5 + 6*(4%6) = 5 + 24 = 29;
        // now for next index calulation we might need the original value of num[0] which can be obtain by num[0]%6 = 29%6 = 5;
        // if we want to get just he new value of num[0], we can get it by num[0]/6 = 29/6 = 4
        // Ref: https://leetcode.com/problems/build-array-from-permutation/discuss/1315926/Python-O(n)-Time-O(1)-Space-w-Full-Explanation
        // https://leetcode.com/problems/build-array-from-permutation/discuss/1316500/Java-solution-using-O(1)-space-with-explanation
        nums[index] = nums[index] + n * (nums[nums[index]] % n)
    }

    // set new values to every index
    for (let index = 0; index < n; index++) {
        nums[index] = parseInt(nums[index] / n);
    }

    return nums
};