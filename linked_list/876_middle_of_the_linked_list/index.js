/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/middle-of-the-linked-list/}
 * @description Given the head of a singly linked list, return the middle node of the linked list.
 * If there are two middle nodes, return the second middle node.
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
const middleNode = function(head) {
    let slow = head
    let fast = head

    // hair and tortose approach
    // one pointer will go 2 steps and another 1 step.
    // So,when faster pointer reaches to the end, slow pointer will reach to the middle
    while (fast && fast.next) {
        slow = slow.next
        fast = fast.next.next
    }

    return slow
};
