/**
 * @param {string} s
 * @return {number}
 */
const numDecodings = function (s) {
  const dp = {};
  dp[s.length] = 1;

  for (let i = s.length - 1; i >= 0; i--) {
    const char = s[i];
    if (char === "0") {
      dp[i] = 0;
    } else {
      dp[i] = dp[i + 1];
    }

    if (
      i + 1 < s.length &&
      (s[i] === "1" || (s[i] === "2" && "0123456".includes(s[i + 1])))
    ) {
      dp[i] += dp[i + 2];
    }
  }

  return dp[0];
};
