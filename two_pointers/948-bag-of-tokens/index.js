/**
 * @param {number[]} tokens
 * @param {number} power
 * @return {number}
 */
const bagOfTokensScore = function (tokens, power) {
  let res = 0;
  let score = 0;
  let l = 0;
  let r = tokens.length - 1;

  tokens.sort((a, b) => a - b);

  while (l <= r) {
    if (power >= tokens[l]) {
      power -= tokens[l];
      score++;
      res = Math.max(res, score);
      l++;
    } else if (score) {
      power += tokens[r];
      score--;
      r--;
    } else {
      break;
    }
  }

  return res;
};
