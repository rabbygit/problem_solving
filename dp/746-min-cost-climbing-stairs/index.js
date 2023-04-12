/**
 * @param {number[]} cost
 * @return {number}
 */
const minCostClimbingStairs = function (cost) {
  cost.push(0);

  for (let index = cost.length - 3; index > -1; index--) {
    cost[index] += Math.min(cost[index + 1], cost[index + 2]);
  }

  return Math.min(cost[0], cost[1]);
};
