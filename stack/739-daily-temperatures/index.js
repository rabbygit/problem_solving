/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
const dailyTemperatures = function (temperatures) {
  const n = temperatures.length;
  const res = new Array(n).fill(0);
  const stack = [[temperatures[n - 1], n - 1]];

  for (let idx = n - 2; idx >= 0; idx--) {
    while (stack.length && stack[stack.length - 1][0] <= temperatures[idx]) {
      stack.pop();
    }

    if (stack.length) {
      res[idx] = stack[stack.length - 1][1] - idx;
    }

    stack.push([temperatures[idx], idx]);
  }

  return res;
};
