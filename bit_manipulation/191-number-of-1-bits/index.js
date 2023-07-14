/**
 * @param {number} n - a positive integer
 * @return {number}
 */
const hammingWeight = function (n) {
  let res = 0;

  while (n) {
    if (1 & n) res++;
    n = n >>> 1;
  }

  return res;
};
