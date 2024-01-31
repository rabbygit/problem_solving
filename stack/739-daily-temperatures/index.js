/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
const dailyTemperatures = function (temperatures) {
  const stack = [];
  const n = temperatures.length;
  const res = new Array(n).fill(0);

  for (let i = 0; i < n; i++) {
    const temperature = temperatures[i];
    while (stack.length && stack[stack.length - 1][1] < temperature) {
      const [idx, _] = stack.pop();
      res[idx] = i - idx;
    }

    stack.push([i, temperature]);
  }

  return res;
};
