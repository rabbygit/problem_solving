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

    if (n > 1) {
        // sort the elements to keep same element side by side like [1,2,3,1] to [1,1,2,3]
        candidates = mergeSort(candidates, 0, n - 1);
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
            // skip duplicate value and move to next element
            if (i != index && candidate === candidates[index - 1]) {
                continue
            }
            sub_result.push(candidate)
            generate_combination(sub_result, sum + candidate, index + 1)
            sub_result.pop()
        }
    }

    generate_combination([], 0, 0)
    return result
};

function merge(arr, l, m, r) {
    let n1 = m - l + 1;
    let n2 = r - m;

    // Create temp arrays
    let L = new Array(n1);
    let R = new Array(n2);

    // Copy data to temp arrays L[] and R[]
    for (let i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (let j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Merge the temp arrays back into arr[l..r]

    // Initial index of first subarray
    let i = 0;

    // Initial index of second subarray
    let j = 0;

    // Initial index of merged subarray
    let k = l;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of
    // L[], if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of
    // R[], if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }

    return arr
}

// l is for left index and r is
// right index of the sub-array
// of arr to be sorted */
function mergeSort(arr, l, r) {
    if (l >= r) {
        return;//returns recursively
    }
    let m = l + parseInt((r - l) / 2);
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    return merge(arr, l, m, r);
}
