/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/top-k-frequent-elements/}
 * @description Given an integer array nums and an integer k, return the k most frequent elements. 
 * You may return the answer in any order.
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const topKFrequent = function (nums, k) {
    const n = nums.length
    const count_map = {}
    const count_array = new Array(n + 1).fill(null).map(() => [])
    const result = []

    // count occurence for each element and keep in hashMap like 1 -> 4
    nums.forEach(num => {
        if (count_map[num] === undefined) count_map[num] = 1
        else count_map[num]++
    });

    // build array for occurence from hashMap. like [ [] , [] , [] , [], [1,2 ..] ]
    for (const [key, value] of Object.entries(count_map)) {
        count_array[value].push(key)
    }

    // build the result
    for (let index = n; index >= 0; index--) {
        for (const num of count_array[index]) {
            result.push(num)
            // check k element is taken already or not
            if (result.length === k) return result;
        }
    }
};