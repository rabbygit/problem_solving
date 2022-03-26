/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/min-stack/}
 * @description Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
 */

class MinStack {
  constructor() {
    this.stack = []
    this.min = []
  }

  /** 
   * @param {number} val
   * @return {void}
   */
  push(val) {
    this.setMin(val)
    this.stack.push(val)
  };

  /**
   * @return {void}
   */
  pop() {
    let val = this.stack.pop()
    this.popMin(val)
  };

  /**
   * @return {number}
   */
  top() {
    return this.stack[this.stack.length - 1]
  };

  /**
   * @return {number}
   */
  getMin() {
    return this.min[this.min.length - 1]
  };

  setMin(val) {
    if (!this.min.length || this.min[this.min.length - 1] >= val) {
      this.min.push(val)
    }
  }

  popMin(val) {
    if (this.min.length && this.min[this.min.length - 1] === val) {
      this.min.pop()
    }
  }
}