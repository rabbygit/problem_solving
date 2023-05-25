/**
 *
 
 * [Problem ref]{@link https://leetcode.com/problems/merge-two-sorted-lists/}
 * @description Merge two sorted linked list
 */

/**
 * Definition for singly-linked list.
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
const mergeTwoLists = function (l1, l2) {
  const result = new ListNode();
  let tail = result;

  // if both list have node
  while (l1 && l2) {
    if (l1.val < l2.val) {
      tail.next = l1;
      l1 = l1.next;
    } else {
      tail.next = l2;
      l2 = l2.next;
    }

    tail = tail.next;
  }

  // if l1 has node
  if (l1) tail.next = l1;

  // if l2 has node
  if (l2) tail.next = l2;

  return result.next;
};
