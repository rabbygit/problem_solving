/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
const canCompleteCircuit = function (gas, cost) {
  const total_gas = gas.reduce((a, b) => a + b, 0);
  const total_cost = cost.reduce((a, b) => a + b, 0);
  if (total_cost > total_gas) return -1;

  let start = 0;
  let total = 0;

  for (let i = 0; i < gas.length; i++) {
    total += gas[i] - cost[i];
    if (total < 0) {
      start = i + 1;
      total = 0;
    }
  }

  return start;
};
