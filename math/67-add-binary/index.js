/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
const addBinary = function (a, b) {
  let result = "";
  let carry = 0;
  let i = a.length - 1;
  let j = b.length - 1;

  while (i > -1 || j > -1 || carry) {
    const sum = (+a[i] || 0) + (+b[j] || 0) + carry;

    // 1 + 1 = 10, 1 + 0 = 1, 1 + 1 + 1 = 11
    if (sum === 3) {
      result = `1${result}`;
      carry = 1;
    } else if (sum === 2) {
      result = `0${result}`;
      carry = 1;
    } else if (sum === 1) {
      result = `1${result}`;
      carry = 0;
    } else {
      result = `0${result}`;
      carry = 0;
    }

    i--;
    j--;
  }

  return result;
};
