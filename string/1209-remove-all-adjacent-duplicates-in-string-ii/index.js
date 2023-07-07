/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
const removeDuplicates = function (s, k) {
  const stack = [];
  let res = "";

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    const currLen = stack.length;
    if (!stack.length || stack[currLen - 1].char !== char) {
      // keep char and its count
      stack.push({ char, count: 1 });
    } else {
      stack[currLen - 1].count++;
      if (stack[currLen - 1].count === k) {
        stack.pop();
      }
    }
  }

  for (const item of stack) {
    res += item.char.repeat(item.count);
  }

  return res;
};
