/**
 * [Problem ref]{@link  https://leetcode.com/problems/add-two-numbers/submissions/}
 */

/**
 * Node class
 * @param val
 * @param next
 */
class ListNode {
  constructor(val = 0, next = null) {
    this.val = val;
    this.next = next;
  }
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = function (l1, l2) {
  let curry = 0;
  let result = null;
  let reverse = null;

  // both list have node
  while (l1 && l2) {
    let sum = l1.val + l2.val + curry;

    if (sum >= 10) {
      sum = sum % 10;
      curry = 1;
    } else {
      curry = 0;
    }

    // create new node and add the node at head
    let new_node = new ListNode(sum, result);
    result = new_node;

    // move forward
    l1 = l1.next;
    l2 = l2.next;
  }

  // l1 has remaining nodes
  while (l1) {
    let sum = l1.val + curry;

    if (sum >= 10) {
      sum = sum % 10;
      curry = 1;
    } else {
      curry = 0;
    }

    // create new node and add the node at head
    let new_node = new ListNode(sum, result);
    result = new_node;

    // move forward
    l1 = l1.next;
  }

  // l2 has remaining nodes
  while (l2) {
    let sum = l2.val + curry;

    if (sum >= 10) {
      sum = sum % 10;
      curry = 1;
    } else {
      curry = 0;
    }

    // create new node and add the node at head
    let new_node = new ListNode(sum, result);
    result = new_node;

    // move forward
    l2 = l2.next;
  }

  // if curry exits
  if (curry) {
    result = new ListNode(curry, result);
    curry = 0;
  }

  // reverse the list
  while (result) {
    let temp = result.next;
    result.next = reverse;
    reverse = result;
    result = temp;
  }

  return reverse;
};