/**
 * @param {string} s
 * @return {string}
 */
const decodeString = function (s) {
  const stack = [];

  for (const char of s) {
    if (char !== "]") {
      stack.push(char);
    } else {
      let substr = "";
      let k = "";

      while (stack.length && stack[stack.length - 1] !== "[") {
        substr = stack.pop() + substr;
      }
      stack.pop(); // pop the '['
      while (stack.length && !isNaN(parseInt(stack[stack.length - 1]))) {
        k = stack.pop() + k;
      }

      stack.push(substr.repeat(parseInt(k)));
    }
  }

  return stack.join("");
};
