/**
 * [Problem ref]{@link  https://leetcode.com/problems/convert-1d-array-into-2d-array/}
 * @description You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. 
 * You are tasked with creating a 2-dimensional (2D) array with m rows and n columns using all the elements from original.
 */

/**
 * @param {number[]} original
 * @param {number} m
 * @param {number} n
 * @return {number[][]}
 */
const construct2DArray = function (original, m, n) {
    const result = []
    const length = original.length
    let row = 0
    let col = 0
    if (m * n != length) {
        return result
    }

    for (let i = 0; i < m; i++) {
        result[i] = new Array(n)
    }

    for (let index = 0; index < length; index++) {
        result[row][col] = original[index]
        col++

        if (col >= n) {
            row = row + 1
            col = 0
        }
    }

    return result
};