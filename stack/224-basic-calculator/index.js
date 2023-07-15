/**
 * @param {string} s
 * @return {number}
 */
const calculate = function (s) {
  let curr = 0;
  let output = 0;
  let sign = 1; // 1 for '+' | -1 for '-'
  const stack = [];

  for (const char of s) {
    if (!isNaN(parseInt(char))) {
      curr = curr * 10 + parseInt(char);
    } else if (["+", "-"].includes(char)) {
      output += curr * sign;
      curr = 0;
      if (char === "+") sign = 1;
      else sign = -1;
    } else if (char === "(") {
      stack.push(output, sign);
      output = 0;
      sign = 1;
    } else if (char === ")") {
      output += curr * sign;
      output *= stack.pop(); // sign
      output += stack.pop(); // last calculated value of the stack
      curr = 0;
    }
  }

  return output + curr * sign;
};
