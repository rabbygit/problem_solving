/**
 * [Problem ref]{@link  https://leetcode.com/problems/remove-linked-list-elements/}
 * @description Remove element from linked list
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
 * @param {number} val
 * @return {ListNode}
 */
const removeElements = function (head, val) {
  let previous = null;
  let current = head;
  let is_head = true;

  while (current) {
    // check the value whether equal
    if (current.val == val) {
      if (is_head) {
        // remove from head
        head = head.next;
      } else if (!current.next) {
        // remove the last node
        previous.next = null;
      } else {
        // remove from middle
        previous.next = current.next
      }
    } else {
      is_head = false; // track head
      previous = current; // track unmatched previous node
    }

    current = current.next;
  }

  return head;
};