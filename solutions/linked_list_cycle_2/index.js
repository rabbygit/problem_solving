/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/linked-list-cycle-ii}
 * @description Given the head of a linked list, return the node where the cycle begins.
 * If there is no cycle, return null.
 * [Explanation]{@link http://www.shafaetsplanet.com/?p=2822}
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const detectCycle = function (head) {
    if (!head || !head.next) return null;

    let slow = head;
    let fast = head;

    while (slow) {
        if (fast && fast.next) {
            slow = slow.next;
            fast = fast.next.next;
        } else {
            return null; // no cycle
        }

        // Cycle detected
        if (slow == fast) break;
    }

    let slow2 = head;
    while (slow2 != slow) {
        slow2 = slow2.next;
        slow = slow.next;
    }

    return slow;
};