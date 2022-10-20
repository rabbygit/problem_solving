/**
 * [Problem ref]{@link  https://leetcode.com/problems/swap-nodes-in-pairs/}
 * @description Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
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
 * @return {ListNode}
 */
const swapPairs = function (head) {
  // return if list has no or one node
  if (!head || !head.next) return head;

  // two pointer
  let slow = head
  let fast = head.next
  let prev = null

  while (slow && fast) {
    let temp = fast.next

    // swap head node
    if (!prev) {
      head = fast
      head.next = slow
      head.next.next = temp
    } else {
      // swap nodes from middle
      prev.next = fast
      prev.next.next = slow
      slow.next = temp
    }

    // keep track of previous node for swaping from the middle of the list
    prev = slow

    // update the pointers to next
    slow = temp
    if (slow) fast = slow.next
  }

  return head
};