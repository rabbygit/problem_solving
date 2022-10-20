/**
 * [Problem ref]{@link https://leetcode.com/problems/min-stack/}
 * @description Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
 */

class MinStack {
  constructor() {
    this.stack = [];
  }

  /**
   * @param {number} val
   * @return {void}
   */
  push(val) {
    let current_min = val;
    if (this.stack.length && this.getTopElement().current_min < val) {
      current_min = this.getTopElement().current_min;
    }
    this.stack.push({ val, current_min });
  }

  /**
   * @return {void}
   */
  pop() {
    this.stack.pop();
  }

  /**
   * @return {number}
   */
  top() {
    return this.getTopElement().val;
  }

  /**
   * @return {number}
   */
  getMin() {
    return this.getTopElement().current_min;
  }

  getTopElement() {
    return this.stack[this.stack.length - 1];
  }
}
