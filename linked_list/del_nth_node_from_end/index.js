/**
 * @author Rabby Hossain
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
  let prev = head;
  let current_node = head;
  let found = false;
  let pass = 1;

  while (current_node) {
    let temp = current_node;

    // Loop through from the current node to end
    // check if current node is the n-th node
    for (let index = 1; index <= n; index++) {
      if (temp.next == null) {
        found = true;
        break;
      }

      temp = temp.next;
    }

    if (found) break;

    // Move forward
    prev = current_node;
    current_node = current_node.next;
    pass++;
  }

  if (pass == 1) {
    // Remove head?
    head = prev.next;
  } else {
    prev.next = prev.next.next
  }

  return head
};