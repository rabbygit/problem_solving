/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
const addStrings = function (num1, num2) {
  num1 = num1.split("").reverse().join("");
  num2 = num2.split("").reverse().join("");
  let result = "";
  let idx = 0;
  let carry = 0;
  const l1 = num1.length;
  const l2 = num2.length;
  const l3 = Math.max(l1, l2);

  while (idx < l3 || carry) {
    const digit1 = idx < l1 ? parseInt(num1[idx]) : 0;
    const digit2 = idx < l2 ? parseInt(num2[idx]) : 0;
    let currSum = digit1 + digit2 + carry;
    carry = parseInt(currSum / 10);
    currSum = currSum % 10;
    result += String(currSum);
    idx++;
  }

  return result.split("").reverse().join("");
};
