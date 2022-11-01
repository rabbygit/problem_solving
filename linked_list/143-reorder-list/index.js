/**
 * [Problem ref]{@link  https://leetcode.com/problems/reorder-list/description/}
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
 * @return {void} Do not return anything, modify head in-place instead.
 */
const reorderList = function (head) {
  // find the middle
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  // cut the link
  let second_part = slow.next;
  slow.next = null;

  // reverse the second part
  let reversed_part = null;
  while (second_part) {
    const temp = second_part.next;
    second_part.next = reversed_part;
    reversed_part = second_part;
    second_part = temp;
  }

  // concate two list
  let first_part = head;
  while (first_part && reversed_part) {
    const temp1 = first_part.next;
    const temp2 = reversed_part.next;

    // link two list
    first_part.next = reversed_part;
    reversed_part.next = temp1;

    // update next pointer
    first_part = temp1;
    reversed_part = temp2;
  }
};
