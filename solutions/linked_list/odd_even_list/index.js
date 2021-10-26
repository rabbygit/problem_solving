/**
 *
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/odd-even-linked-list/}
 * @description Given the head of a singly linked list, 
 * group all the nodes with odd indices together 
 * followed by the nodes with even indices,
 * and return the reordered list.
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
const oddEvenList = function (head) {
    // If list contains no nodes or only two nodes
    if (!head || !head.next) {
        return head;
    }

    let prev_odd = head; // 1st node
    let prev_even = head.next; // 2nd node

    let current_odd = null;
    let current_even = null;
    let first_even = head.next;

    if (prev_even.next) {
        current_odd = prev_even.next; // 3rd node
    }

    if (current_odd && current_odd.next) {
        current_even = current_odd.next; // 4th node
    }


    while (current_odd || current_even) {

        // link current odd and even position node with
        // previous odd and even nodes
        prev_odd.next = current_odd;
        prev_even.next = current_even;

        // move forward the prevous odd position's node
        prev_odd = prev_odd.next;
        // move forward the prevous even position's node
        prev_even = prev_even.next;

        // move forward the current odd position
        if (current_odd.next && current_odd.next.next) {
            current_odd = current_odd.next.next;
        } else {
            current_odd = null;
        }

        // move forward the current even position
        if (current_even && current_even.next && current_even.next.next) {
            current_even = current_even.next.next;
        } else {
            current_even = null;
        }
    }

    // link last odd node to first even node
    prev_odd.next = first_even;

    // return ordered head
    return head;
};