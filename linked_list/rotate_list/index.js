/**
 
 * @description rotate linked to list to right
 * [Problem ref]{@link  https://leetcode.com/problems/rotate-list/} 
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
 * @param {number} k
 * @return {ListNode}
 */
const rotateRight = function (head, k) {
  let size = 0;
  let index = 1;
  let current = head;
  let previous = null;

  // determine the size of linked list
  while (current) {
    size++
    current = current.next;
  }

  // return head for invalid value
  if (!size || size === 1 || !k || !(k % size)) return head;

  // split the list in two part
  let flag = size - k % size; // where to split
  current = head;
  while (index <= flag) {
    previous = current;
    current = current.next;
    index++;
  }

  // last node of the splitted-list's left part
  // and make it the last node of final list
  previous.next = null;

  // loop through to the last node of the splitted-list's right part
  // and place right part in front of the linked list
  let temp = current;
  while (temp.next) {
    temp = temp.next
  }
  temp.next = head

  return current; // final list
};