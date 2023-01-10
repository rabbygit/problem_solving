/**
 * [Problem ref]{@link https://leetcode.com/problems/plus-one/}
 * @param {number[]} digits
 * @return {number[]}
 */
const plusOne = function (digits) {
    let hold = 1;

    for (let index = digits.length - 1; index >= 0; index--) {
        const sum = digits[index] + hold;
        if (sum === 10) {
            digits[index] = 0;
            hold = 1;
        } else {
            digits[index] = sum;
            hold = 0;
        }
    }

    if (hold) {
        digits.unshift(hold)
    }

    return digits
};