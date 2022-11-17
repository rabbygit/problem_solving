/**
 * [Problem ref]{@link  https://leetcode.com/problems/lru-cache/}
 * @description Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
 */

class Node {
  constructor(key, value) {
    this.key = key;
    this.value = value;
    this.previous = null;
    this.next = null;
  }
}

class LRUCache {
  /**
   * @param {number} capacity
   */
  constructor(capacity) {
    this.capacity = capacity;
    this.track_node = new Map();

    // left = LRU and right = most recent node
    // put all nodes between this two nodes, will make code clean
    this.left = new Node(0, 0);
    this.right = new Node(0, 0);
    this.left.next = this.right;
    this.right.previous = this.left;
  }

  /**
   * @param {number} key
   * @return {number}
   */
  get(key) {
    const node = this.track_node.get(key);

    if (node) {
      // remove and move the node to right most position
      this.remove_from_middle(node);
      this.move_to_first(node);

      // return the value
      return node.value;
    }

    // if not present in cache return -1
    return -1;
  }

  /**
   * @param {number} key
   * @param {number} value
   * @return {void}
   */
  put(key, value) {
    const found_node = this.track_node.get(key);

    // if cache already has this key, then remove it
    if (found_node) {
      this.remove_from_middle(found_node);
    }

    // else, create new node and move to right
    const node = new Node(key, value);
    this.track_node.set(key, node);
    this.move_to_first(node);

    // if cache capacity exceeds, remove from left
    if (this.track_node.size > this.capacity) {
      this.remove_from_middle(this.left.next);
      this.track_node.delete(this.left.next.key);
    }
  }

  /**
   * @description prepend a node at first position of the list
   * @param {*} new_node
   * @returns
   */
  move_to_first(node) {
    const prev = this.right.previous;
    prev.next = node;
    this.right.previous = node;
    node.previous = prev;
    node.next = this.right;
  }

  /**
   * @description remove node from middle of the list
   * @param {*} node
   */
  remove_from_middle(node) {
    node.previous.next = node.next;
    node.next.previous = node.previous;
  }
}
