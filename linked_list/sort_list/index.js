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
const sortList = function (head) {
    if (!head || !head.next) return head;
    return mergeSort(head);
};


/**
 * @description sort a list
 * @param {ListNode} head 
 * @returns {ListNode}
 */
function mergeSort(head) {
    // Base case from where single node return
    if (!head || !head.next) {
        return head;
    }

    // Find the middle  of the list
    let middle = findMiddle(head);
    let middle_next = middle.next;
    middle.next = null;

    // call left and right part of the list recursively
    let left_part = mergeSort(head);
    let right_part = mergeSort(middle_next);

    // sort and merge two part
    // return to previous call
    return merge(left_part, right_part);
}

/**
 * @description  Find middle of the linked list
 * @param {ListNode} head
 * @returns {ListNode}
 */
function findMiddle(head) {
    let slow = head;
    let fast = head;

    while (fast.next && fast.next.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    return slow;
}

/**
 * @description sort and merge two list
 * @param {ListNode} head1 
 * @param {ListNode} head2 
 * @returns {ListNode}
 */
function merge(head1, head2) {
    if (!head1) return head2;
    if (!head2) return head1;

    let result = null;
    if (head1.val <= head2.val) {
        result = head1;
        result.next = merge(head1.next, head2);
    } else {
        result = head2;
        result.next = merge(head1, head2.next);
    }

    return result;
}
