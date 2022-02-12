/**
 * @author Rabby Hossain
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
const swapPairs = function(head) {
    if (!head) return  head

    let slow = head
    let fast = head.next

    while (slow && fast) {
        let temp = fast.next
        slow.next = temp
        fast.next = slow

      if (slow.next) slow = slow.next.next
      if(fast.next) fast = fast.next.next
    }

    return head
};