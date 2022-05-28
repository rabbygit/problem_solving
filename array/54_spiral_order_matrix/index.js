/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/spiral-matrix/}
 * @description Given an m x n matrix, return all elements of the matrix in spiral order.
 */

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
const spiralOrder = function (matrix) {
    const result = []
    const m = matrix.length
    if (m === 0) {
        return result
    }

    let left = 0
    let top = 0
    let right = matrix[0].length - 1
    let bottom = m - 1

    let direction = 0

    while (left <= right && top <= bottom) {
        // traverse left to right
        if (direction === 0) {
            for (let index = left; index <= right; index++) {
                result.push(matrix[top][index])
            }
            // increase top boundary
            top++;
        } else if (direction === 1) {
            // traverse top to bottom
            for (let index = top; index <= bottom; index++) {
                result.push(matrix[index][right])
            }
            // decrease right boundary
            right--;
        } else if (direction === 2) {
            // traverse right to left
            for (let index = right; index >= left; index--) {
                result.push(matrix[bottom][index])
            }
            // decrease bottom boundary
            bottom--;
        } else {
            // traverse bottom to top
            for (let index = bottom; index >= top; index--) {
                result.push(matrix[index][left])
            }
            // increase left boundary
            left++;
        }

        direction = (direction + 1) % 4
    }

    return result
};
