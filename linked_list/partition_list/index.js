/**
 * [Problem ref]{@link  https://leetcode.com/problems/partition-list/}
 * @description Given the head of a linked list and a value x,
 *  partition it such that all nodes less than x come before
 *  nodes greater than or equal to x.
 */

/**
 * Definition for singly-linked list.
 */
function ListNode(val, next) {
  this.val = (val === undefined ? 0 : val);
  this.next = (next === undefined ? null : next);
}

/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
const partition = function (head, x) {

  // If head has no or single node
  if (!head || !head.next) return head;

  let temp_list = null;
  let previous = null;
  let reversed = null;
  let runner = head;

  // filter out node which has large value than x
  while (runner) {
    if (runner.val >= x) {
      temp_list = new ListNode(runner.val, temp_list);
      if (!previous) {
        head = runner.next;
      } else if (runner.next) {
        previous.next = runner.next;
      } else {
        previous.next = null;
      }
    } else {
      previous = runner;
    }
    runner = runner.next;
  }

  // reverse the new list
  while (temp_list) {
    let temp = temp_list.next;
    temp_list.next = reversed;
    reversed = temp_list;
    temp_list = temp;
  }

  // add two list
  if (previous) previous.next = reversed;
  else head = reversed;

  return head;
};

/**
 * Note: There is another way, creating two separate list
 * instead of keeping it in original list
 */