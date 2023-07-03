/**
 * @param {number[][]} costs
 * @return {number}
 */
const twoCitySchedCost = function (costs) {
  let sum = 0;
  let totalA = costs.length / 2;
  let totalB = costs.length / 2;

  for (let i = 0; i < costs.length; i++) {
    const [a, b] = costs[i];
    if (a < b && totalA) {
      sum += a;
      totalA--;
    } else if (!totalB) {
      sum += a;
      totalA--;
    } else {
      sum += b;
      totalB--;
    }
  }

  return sum;
};
