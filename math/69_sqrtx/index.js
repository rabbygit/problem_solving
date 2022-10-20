/**
 * [Problem ref]{@link https://leetcode.com/problems/sqrtx/}
 * @description Given a non-negative integer x, compute and return the square root of x.
 */


/**
 * @param {number} x
 * @return {number}
 */
const mySqrt = function (x) {
    return findSqrt(x, 1, x)
};

/**
 * @description idea is comparing the mid value, if mid * mid is high then we will try with lower value than mid else higher
 * @param {*} n num to compare
 * @param {*} left min boundary
 * @param {*} right max boundary
 * @returns 
 */
function findSqrt(n, left, right) {
    if (left > right) return right

    let mid = parseInt((left + right) / 2)

    if (mid * mid === n) {
        return mid
    } else if (mid * mid > n) {
        return findSqrt(n, left, mid - 1)
    } else {
        return findSqrt(n, mid + 1, right)
    }
}