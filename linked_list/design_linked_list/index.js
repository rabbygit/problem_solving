/**
 *
 
 * [Problem ref]{@link https://leetcode.com/problems/design-linked-list/}
 * @description Design a likedlist
 */

/**
 * Node class
 */
class Node {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

/**
 * Initialize your data structure here.
 */
class MyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = -1;
  }
};

/**
 * Get the value of the index-th node in the linked list. If the index is invalid, return -1. 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function (index) {
  // check valid index
  if (this.length === -1 || index > this.length) {
    return -1
  } else if (!index) {
    return this.head.val;
  }

  // Otherwise,loop through to that element and return the value
  let value;
  let current_position = this.head.next;
  for (let i = 1; i <= index; i++) {
    value = current_position.val;
    current_position = current_position.next;
  }

  return value;
};

/**
 * Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function (val) {
  // create new node 
  let new_node = new Node(val, this.head);
  this.head = new_node;
  if (this.length === -1) {
    this.tail = new_node;
  }
  this.length++;
};

/**
 * Append a node of value val to the last element of the linked list. 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function (val) {
  // create new node
  let new_node = new Node(val);
  if (this.length === -1) {
    // List is empty.add to list as first node
    this.head = new_node;
    this.tail = new_node;
  } else {
    // add the new_node to last element's next attribute.
    this.tail.next = new_node;
    this.tail = this.tail.next;
  }
  this.length++;
};

/**
 * Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function (index, val) {
  if (index - 1 > this.length || index <= -1) {
    return;
  } else if (!index) {
    // Add to head
    this.addAtHead(val);
  } else if (index - 1 === this.length) {
    // add to  last element
    this.addAtTail(val);
  } else {
    // add to nth node's previous node
    let current_node = this.head;
    let new_node;
    let previous;
    for (let i = 0; i < index; i++) {
      previous = current_node; // track previous node
      current_node = current_node.next; // next node
      new_node = new Node(val, current_node); // create new node with next node
    }
    previous.next = new_node;
    this.length++;
  }
};

/**
 * Delete the index-th node in the linked list, if the index is valid. 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function (index) {
  if (index > -1 && index <= this.length) {
    // valid index
    if (!index) {
      if (!this.length) {
        // List has one node
        this.head = null;
        this.tail = null;
      } else {
        this.head = this.head.next;
      }
    } else if (index === this.length) {
      // delete the last element
      let current_node = this.head;
      for (let i = 0; i < index - 1; i++) {
        current_node = current_node.next; // next node
      }
      current_node.next = null;
      this.tail = current_node;
    } else {
      // delete nth element
      let current_node = this.head;
      let previous;
      for (let i = 0; i <= index - 1; i++) {
        previous = current_node;
        current_node = current_node.next; // next node
      }
      previous.next = current_node.next;
    }
    this.length--;
  }
};