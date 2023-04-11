/**
 * @param {number} n
 * @return {number}
 */
const climbStairs = function (n) {
  let oneStep = 1;
  let twoStep = 1;

  for (let index = 0; index < n - 1; index++) {
    let temp = oneStep;
    oneStep = oneStep + twoStep;
    twoStep = temp;
  }

  return oneStep;
};
