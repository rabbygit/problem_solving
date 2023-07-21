/**
 * @param {number[]} baseCosts
 * @param {number[]} toppingCosts
 * @param {number} target
 * @return {number}
 */
const closestCost = function (baseCosts, toppingCosts, target) {
  let result = Number.MAX_SAFE_INTEGER;
  let diff = Number.MAX_SAFE_INTEGER;

  function dfs(idx, curr) {
    if (Math.abs(curr - target) < diff) {
      result = curr;
      diff = Math.abs(curr - target);
    }

    if (Math.abs(curr - target) === diff) {
      result = Math.min(result, curr);
    }

    if (idx >= toppingCosts.length || curr - target > diff) {
      return;
    }

    dfs(idx + 1, curr + toppingCosts[idx]);
    dfs(idx + 1, curr + 2 * toppingCosts[idx]);
    dfs(idx + 1, curr);
  }

  for (let i = 0; i < baseCosts.length; i++) {
    dfs(0, baseCosts[i]);
  }

  return result;
};
