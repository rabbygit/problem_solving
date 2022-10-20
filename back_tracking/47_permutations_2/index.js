/**
 * [Problem ref]{@link https://leetcode.com/problems/permutations-ii/}
 * @description Given a collection of numbers, nums, that might contain duplicates,
 * return all possible unique permutations in any order.
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const permuteUnique = function (nums) {
    const result = [];
    const unique = {};
    const n = nums.length;

    // make unique elemets hash with number of occurrence
    for (let index = 0; index < nums.length; index++) {
        const element = nums[index];
        if (unique[element] === undefined) {
            unique[element] = 1
        } else {
            unique[element]++
        }
    }


    // generate unique permutation
    function genratePermute(sub_result) {
        if (sub_result.length === n) {
            result.push([...sub_result]);
            return;
        }

        // loop through each key
        Object.keys(unique).forEach(element => {
            // check all occurenece is used or not
            if (unique[element] > 0) {
                unique[element]--; // decrease occurence count
                sub_result.push(Number(element)) // push to sub result array
                genratePermute(sub_result) // recurse
                sub_result.pop() // pop last element
                unique[element]++ // increase occurence
            }
        })
    }

    genratePermute([]);

    return result;
};