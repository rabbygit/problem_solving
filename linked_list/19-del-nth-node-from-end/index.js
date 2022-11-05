/**
 * [Problem ref]{@link  https://leetcode.com/problems/remove-nth-node-from-end-of-list}
 * @description Remove n-th node from linked list in one pass
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
const removeNthFromEnd = function (head, n) {
  let dummy = new ListNode(0, head);
  let left = dummy;
  let right = head;

  // difference between left and right pointer is n
  // so, when right go to end of the list, left will point to the nth node
  while (n > 0 && right) {
    right = right.next;
    n--;
  }

  while (right) {
    left = left.next;
    right = right.next;
  }

  // remove the nth node
  left.next = left.next.next;

  return dummy.next;
};
