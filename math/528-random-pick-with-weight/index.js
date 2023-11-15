class Solution {
  /**
   * @param {number[]} w
   */
  constructor(w) {
    this.w = w;
    const total = this.w.reduce((a, b) => a + b, 0);

    // find possibility for each weight
    for (let i = 0; i < this.w.length; i++) {
      this.w[i] = this.w[i] / total;
    }

    // range the possibility
    for (let i = 1; i < this.w.length; i++) {
      this.w[i] += this.w[i - 1];
    }
  }

  getRandomFloat(min, max) {
    return Math.random() * (max - min) + min;
  }

  /**
   * @return {number}
   */
  pickIndex() {
    const possbility = this.getRandomFloat(0, 1);
    for (let i = 0; i < this.w.length; i++) {
      if (this.w[i] >= possbility) {
        return i;
      }
    }
  }
}
