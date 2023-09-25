/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
const convert = function (s, numRows) {
  if (numRows === 1) return s;
  const res = new Array(numRows).fill("");
  let going_up = true;
  let idx = 1;

  for (const char of s) {
    res[idx - 1] += char;
    if (idx === numRows) {
      going_up = false;
    } else if (idx === 1) {
      going_up = true;
    }

    if (going_up) {
      idx++;
    } else {
      idx--;
    }
  }

  return res.join("");
};
