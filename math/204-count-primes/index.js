/**
 * @param {number} n
 * @return {number}
 */
const countPrimes = function (n) {
  if (n < 2) return 0;
  const composits = new Array(n).fill(false);
  let result = 0;

  for (let i = 2; i <= parseInt(Math.sqrt(n)); i++) {
    if (!composits[i]) {
      for (let j = i * i; j < n; j += i) {
        composits[j] = true;
      }
    }
  }

  for (let i = 2; i < n; i++) {
    if (!composits[i]) result++;
  }

  return result;
};
