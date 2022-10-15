/**
 * [Problem ref]{@link https://leetcode.com/problems/evaluate-reverse-polish-notation/}
 * @description Evaluate the value of an arithmetic expression in Reverse Polish Notation.
 * Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
 * Note that division between two integers should truncate toward zero.
 * It is guaranteed that the given RPN expression is always valid.
 * That means the expression would always evaluate to a result,
 * and there will not be any division by zero operation.
 */

/**
 * @param {string[]} tokens
 * @return {number}
 */
const evalRPN = function (tokens) {
  const stack = [];

  for (const token of tokens) {
    if (isNaN(token)) {
      const num1 = stack.pop();
      const num2 = stack.pop();
      stack.push(evaluate(num1, num2, token));
    } else {
      stack.push(Number(token));
    }
  }

  return stack.pop();
};

const evaluate = (num1, num2, operand) => {
  if (operand === "+") {
    return num1 + num2;
  } else if (operand === "-") {
    return num2 - num1;
  } else if (operand === "*") {
    return num2 * num1;
  } else {
    return parseInt(num2 / num1);
  }
};