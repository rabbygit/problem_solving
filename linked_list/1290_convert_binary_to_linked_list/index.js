
/**
 * [Problem ref]{@link  https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/}
 * @description Given head which is a reference node to a singly-linked list. 
 * The value of each node in the linked list is either 0 or 1. 
 * The linked list holds the binary representation of a number.
 * Return the decimal value of the number in the linked list.
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
 * @return {number}
 */
const getDecimalValue = function(head) {
    let str = ''
    while (head) {
        str += head.val
        head = head.next
    }

    return parseInt(str, 2)
};