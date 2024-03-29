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
const oddEvenList = function (head) {
  // If list contains no nodes or only two nodes
  if (!head || !head.next) {
    return head;
  }

  let odd = head;
  let even = head.next;
  let odd_head = head;
  let even_head = head.next;

  while (even && even.next) {
    odd.next = odd.next.next;
    even.next = even.next.next;
    odd = odd.next;
    even = even.next;
  }

  odd.next = even_head;

  return odd_head;
};
