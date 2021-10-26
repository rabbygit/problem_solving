/**
 *
 * @author Rabby Hossain
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
  let result = null;
  let reverse = null;

  // if both list have node
  while (l1 && l2) {
    let val;
    if (l1.val >= l2.val) {
      val = l2.val;
      l2 = l2.next;
    } else {
      val = l1.val;
      l1 = l1.next;
    }

    result = new ListNode(val, result); // add the small val to result list
  }

  // if l1 has node
  while (l1) {
    result = new ListNode(l1.val, result); // add the val to result list
    l1 = l1.next; // move forward
  }

  // if l2 has node
  while (l2) {
    result = new ListNode(l2.val, result); // add the val to result list
    l2 = l2.next; // move forward
  }

  // reverse the result list
  while (result) {
    let temp = result.next;
    result.next = reverse;
    reverse = result;
    result = temp;
  }

  return reverse;
};