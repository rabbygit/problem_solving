/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/palindrome-linked-list/}
 * @deescription Given the head of a singly linked list, return true if it is a palindrome.
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
 * @return {boolean}
 */
const isPalindrome = function (head) {
  if (!head || !head.next) return true;

  let fast = head;
  let slow = head;
  let reversed = null;

  // find the middle
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  // set null to the end of the right half
  reversed = slow;
  slow = slow.next;
  reversed.next = null;

  // reverse the right half of the list
  while (slow) {
    let temp = slow.next;
    slow.next = reversed;
    reversed = slow;
    slow = temp;
  }

  // compare two halves of the list
  while (head && reversed) {
    if (head.val !== reversed.val) {
      return false;
    } else {
      head = head.next;
      reversed = reversed.next;
    }
  }

  return true;
};