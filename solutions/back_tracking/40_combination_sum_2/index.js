/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/combination-sum-ii/}
 * @description Given a collection of candidate numbers (candidates) and a target number (target),
 * find all unique combinations in candidates where the candidate numbers sum to target.
 * Each number in candidates may only be used once in the combination.
 * Note: The solution set must not contain duplicate combinations.
 */

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
const combinationSum2 = function (candidates, target) {
    const result = []
    const n = candidates.length
    const element_map = {}

    for (let index = 0; index < candidates.length; index++) {
        const element = candidates[index];
        if (element_map[element] === undefined) {
            element_map[element] = 1
        } else {
            element_map[element]++
        }
    }

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
            i++
            generate_combination(sub_result, sum, i)
            sub_result.pop()
            sum -= candidate
        }
    }

    generate_combination([], 0, 0)

    return result
};

console.log(combinationSum2([2, 5, 2, 1, 2], 5));