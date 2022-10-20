/**
 * [Problem ref]{@link https://leetcode.com/problems/reverse-linked-list-ii/}
 * @description Given the head of a singly linked list and two integers left and right where left <= right, 
 * reverse the nodes of the list from position left to position right, and return the reversed list.
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
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
const reverseBetween = function (head, left, right) {
    let count = 1 // track start and end point to reverse
    let start = null // starting node
    let prev_start = null // previous node of starting point
    let end = null // end node
    let next_end = null // next node of ending node
    let prev = null // previous node of any node
    let runner = head

    // loop through until reach to the end point
    while (count <= right) {
        let next = runner.next // keep the next pointer

        // starting point
        if (count === left) {
            start = runner
            prev_start = prev
        }

        // middle nodes between start and end point
        // change pointer of the current node to its previous node
        if (count > left && count < right) runner.next = prev

        // ending point
        if (count === right) {
            end = runner
            next_end = runner.next
            runner.next = prev
        }


        prev = runner
        runner = next
        count++
    }

    start.next = next_end // starting node's will point to the end node's next

    // previous node of starting point(if it's not the beginning of list) 
    // will point to the end node of reversed portion. 
    // otherwise, replace head pointer with the end node of reversed portion
    if (prev_start) prev_start.next = end
    else head = end

    return head
};