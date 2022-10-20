/**
 * [Problem ref]{@link  https://leetcode.com/problems/longest-consecutive-sequence/}
 * @description Given an unsorted array of integers nums, 
 * return the length of the longest consecutive elements sequence.
 * You must write an algorithm that runs in O(n) time.
 */


/**
 * @param {number[]} nums
 * @return {number}
 */
const longestConsecutive = function (nums) {
    const nums_exists = {}
    let longest_sequence = 0

    // create the hash with each elements
    nums.forEach(num => {
        nums_exists[num] = true
    });


    for (let index = 0; index < nums.length; index++) {
        // find the beginning of the sequence and
        // check if its following num does exists
        if (!nums_exists[nums[index] - 1]) {
            let current_num = nums[index]
            let sequence_length = 1
            while (nums_exists[current_num + 1]) {
                current_num += 1
                sequence_length += 1
            }

            longest_sequence = Math.max(sequence_length, longest_sequence)
        }
    }

    return longest_sequence;
};