/**
 * [Problem ref]{@link  https://leetcode.com/problems/linked-list-cycle}
 * @description Given head, the head of a linked list, determine if the linked list has a cycle in it.
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
 * @return {boolean}
 * @description without floyd cycle detection algorithm
 */
const hasCycle = function (head) {
    if (!head || !head.next) return false;

    while (head) {
        if (head.visited) return true

        head.visited = true;
        head = head.next
    }

    return false;
};