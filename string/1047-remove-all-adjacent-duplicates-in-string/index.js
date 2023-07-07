/**
 * @param {string} s
 * @return {string}
 */
const removeDuplicates = function (s) {
  let i = 0;
  let res = s;

  while (i < res.length) {
    if (i >= 0 && i + 1 < res.length && res[i] === res[i + 1]) {
      res = res.slice(0, i) + res.slice(i + 2);
      i = i - 1;
    } else {
      i++;
    }
  }

  return res;
};

const removeDuplicatesStack = function (s) {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (stack.length && stack[stack.length - 1] === char) {
      stack.pop();
    } else {
      stack.push(char);
    }
  }

  return stack.join("");
};
