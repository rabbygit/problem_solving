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
  let result = new ListNode();
  let tail = result;

  // both list have node
  while (l1 && l2) {
    let sum = l1.val + l2.val + curry;

    if (sum >= 10) {
      sum = sum % 10;
      curry = 1;
    } else {
      curry = 0;
    }

    // create new node and add the node at end
    tail.next = new ListNode(sum);
    tail = tail.next;

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

    // create new node and add the node at end
    tail.next = new ListNode(sum);
    tail = tail.next;

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

    // create new node and add the node at end
    tail.next = new ListNode(sum);
    tail = tail.next;

    // move forward
    l2 = l2.next;
  }

  // if curry exits
  if (curry) {
    tail.next = new ListNode(curry);
    curry = 0;
  }

  return result.next;
};
