/**
 * @param {string} s
 * @return {boolean}
 */
const checkValidString = function (s) {
  let openMin = 0;
  let openMax = 0;

  for (const c of s) {
    if (c === "(") {
      openMin++;
      openMax++;
    } else if (c === ")") {
      openMin--;
      openMax--;
    } else {
      openMin--;
      openMax++;
    }

    if (openMin < 0) openMin = 0;
    if (openMax < 0) return false;
  }

  return openMin == 0;
};
