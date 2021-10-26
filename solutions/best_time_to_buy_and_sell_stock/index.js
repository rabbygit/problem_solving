/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = function (prices) {
    let max = 0;
    let min = 0;
    let sum = 0;

    for (let index = 0; index < prices.length - 1; index++) {
        for (let j = index + 1; j < prices.length; j++) {
            if (sum < prices[j] - prices[index]) {
                sum = prices[j] - prices[index]
                min = index
                max = j
            }
        }
    }

    if (max > min) {
        return prices[max] - prices[min]
    }

    return 0;
};

console.log(maxProfit([2, 4, 1]))

// Input: prices = [7, 1, 5, 3, 6, 4] , [2, 4, 1] = 2
// Output: 5
// Explanation: Buy on day 2(price = 1) and sell on day 5(price = 6), profit = 6 - 1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.