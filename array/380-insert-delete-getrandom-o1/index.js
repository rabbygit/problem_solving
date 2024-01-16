class RandomizedSet {
  constructor() {
    this.values = [];
    this.valueMap = new Map();
  }

  /**
   * @param {number} val
   * @return {boolean}
   */
  insert(val) {
    if (!this.valueMap.has(val)) {
      this.values.push(val);
      this.valueMap.set(val, this.values.length - 1);
      return true;
    }

    return false;
  }

  /**
   * @param {number} val
   * @return {boolean}
   */
  remove(val) {
    if (this.valueMap.has(val)) {
      // swap values
      const removedIdx = this.valueMap.get(val);
      const lastValue = this.values[this.values.length - 1];
      this.values[removedIdx] = lastValue;
      this.valueMap.set(lastValue, removedIdx);
      this.values.pop();

      // remove from map
      this.valueMap.delete(val);
      return true;
    }

    return false;
  }

  /**
   * @return {number}
   */
  getRandom() {
    const randomIdx = Math.floor(Math.random() * this.values.length);
    return this.values[randomIdx];
  }
}
/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
