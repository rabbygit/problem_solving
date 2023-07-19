/**
 * @param {number[][]} properties
 * @return {number}
 */
const numberOfWeakCharacters = function (properties) {
  let ans = 0;
  let curMax = 0;
  properties.sort((a, b) => (b[0] === a[0] ? a[1] - b[1] : b[0] - a[0]));

  properties.forEach(([_, d]) => (d < curMax ? ans++ : (curMax = d)));

  return ans;
};
