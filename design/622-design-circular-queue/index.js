/**
 * @param {number} k
 */
class MyCircularQueue {
  constructor(k) {
    this.size = k;
    this.currSize = 0;
    this.headIdx = 0;
    this.queue = new Array(k).fill(0);
  }

  enQueue(value) {
    if (this.isFull()) return false;

    const insertIdx = (this.headIdx + this.currSize) % this.size;
    this.queue[insertIdx] = value;
    this.currSize++;
    return true;
  }

  deQueue() {
    if (this.isEmpty()) return false;

    this.headIdx = (this.headIdx + 1) % this.size;
    this.currSize--;
    return true;
  }

  Front() {
    if (this.isEmpty()) return -1;

    return this.queue[this.headIdx];
  }

  Rear() {
    if (this.isEmpty()) return -1;

    const lastElIdx = (this.headIdx + this.currSize - 1) % this.size;
    return this.queue[lastElIdx];
  }

  isEmpty() {
    return this.currSize === 0;
  }

  isFull() {
    return this.currSize === this.size;
  }
}
