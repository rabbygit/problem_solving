/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
const coinChange = function (coins, amount) {
  const dp = new Array(amount + 1).fill(Number.POSITIVE_INFINITY);
  dp[0] = 0;

  for (let am = 0; am < amount + 1; am++) {
    for (const coin of coins) {
      if (am - coin >= 0) {
        dp[am] = Math.min(dp[am], 1 + dp[am - coin]);
      }
    }
  }

  if (dp[amount] === Number.POSITIVE_INFINITY) {
    return -1;
  }

  return dp[amount];
};
