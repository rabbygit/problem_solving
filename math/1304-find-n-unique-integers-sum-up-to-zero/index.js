/**
 * @param {number} n
 * @return {number[]}
 */
const sumZero = function (n) {
  const result = [];

  // odd number
  if (n % 2) result.push(0);

  for (let i = 0; i < parseInt(n / 2); i++) {
    const n = i + 1;
    result.push(n, -1 * n);
  }

  return result;
};
