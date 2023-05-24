/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
const countOdds = function (low, high) {
  if (low % 2 !== 0 || high % 2 !== 0) {
    return parseInt((high - low) / 2) + 1;
  }

  return parseInt((high - low) / 2);
};
