/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/reverse-nodes-in-k-group/}
 * @description Given a linked list, 
 * reverse the nodes of a linked list k at a time 
 * and return its modified list.
 */

/**
 * Definition for singly-linked list.
 */
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
const reverseKGroup = function (head, k) {
    if (!head || !head.next || k == 1) {
        return head;
    }

    // find the length of the 
    let slow = head;
    let fast = head;
    let counter = 1;
    let length = 0;
    while (fast.next && fast.next.next) {
        counter++;
        slow = slow.next;
        fast = fast.next.next;
    }

    if (!fast.next) {
        length = counter * 2 - 1
    } else {
        length = counter * 2
    }

    let i = length - length % k;
    counter = 1;

    let dummy_head = new ListNode(0);
    dummy_head.next = head;
    let start = dummy_head;
    let end = head;

    while (counter <= i) {

        if (!(counter % k)) {
            start = reverse(start, end.next);
            end = start.next;
        } else {
            end = end.next;
        }

        counter++;
    }

    return dummy_head.next;
};

/**
 * @description Reverse a linked_list portion and return the new starting point
 * @param {ListNode} start
 * @param {ListNode} end
 * @returns {ListNode}
 */
const reverse = function (start, end) {
    let prev = start;
    let current = start.next;
    let first = current;

    while (current != end) {
        let temp = current.next;
        current.next = prev;
        prev = current;
        current = temp;
    }

    start.next = prev; // connect the reversed part with previous start point
    first.next = current; // new starting point
    return first;
}