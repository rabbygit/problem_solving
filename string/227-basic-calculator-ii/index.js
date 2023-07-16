/**
 * @param {string} s
 * @return {number}
 */
const calculate = function (s) {
  let l = 0,
    prev = 0,
    res = 0,
    curr = 0,
    last_op = "+";

  while (l < s.length) {
    if (!isNaN(parseInt(s[l]))) {
      while (l < s.length && !isNaN(parseInt(s[l]))) {
        curr = curr * 10 + parseInt(s[l]);
        l++;
      }
      l--;
      if (last_op === "+") {
        res += curr;
        prev = curr;
      } else if (last_op === "-") {
        res -= curr;
        prev = -curr;
      } else if (last_op === "*") {
        res -= prev;
        res += prev * curr;
        prev = prev * curr;
      } else if (last_op === "/") {
        res -= prev;
        res += parseInt(prev / curr);
        prev = parseInt(prev / curr);
      }
      curr = 0;
    } else if (s[l] !== " ") {
      last_op = s[l];
    }
    l++;
  }

  return res;
};
