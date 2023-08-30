/**
 * @param {number[]} piles
 * @return {number}
 */
const maxCoins = function (piles) {
  piles.sort((a, b) => b - a);
  const n = parseInt(piles.length / 3);
  let result = 0;

  for (let i = 0; i < n; i++) {
    result += piles[i * 2 + 1];
  }

  return result;
};
