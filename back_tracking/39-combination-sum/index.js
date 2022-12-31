/**
 * [Problem ref]{@link https://leetcode.com/problems/combination-sum/}
 * @description Given an array of distinct integers candidates and a target integer target, 
 * return a list of all unique combinations of candidates where the chosen numbers sum to target.
 *  You may return the combinations in any order.
 */

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
const combinationSum = function (candidates, target) {
    const result = []
    const n = candidates.length

    function generate_combination(sub_result, sum, i) {
        if (sum === target) {
            result.push([...sub_result])
            return
        }

        if (sum > target) {
            return
        }

        for (let index = i; index < n; index++) {
            const candidate = candidates[index]
            sub_result.push(candidate)
            sum += candidate
            generate_combination(sub_result, sum, i)
            i++
            sub_result.pop()
            sum -= candidate
        }
    }

    generate_combination([], 0, 0)

    return result
};