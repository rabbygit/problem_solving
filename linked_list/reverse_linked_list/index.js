/**
 * [Problem ref]{@link  https://leetcode.com/problems/reverse-linked-list/}
 * @description Reverse a linked list
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
const reverseList = function (head) {
    let reverse_list = null;

    // Reverse the originnal list
    while (head) {
        let temp = head.next;
        head.next = reverse_list;
        reverse_list = head;
        head = temp
    }

    return reverse_list;
};