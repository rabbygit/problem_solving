/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function (n) {
    let dp = []
    dp[0] = dp[1] = 1;

    for (let len = 2; len <= n; ++len) {
        dp[len] = 0
        console.log(len);
        console.log(dp);
        for (let i = 0; i < len; ++i) {
            dp[len] += dp[i] * dp[len - 1 - i];
        }
    }
    console.log(dp);
    return dp[n];
};

console.log(numTrees(3));