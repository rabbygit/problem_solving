
/**
 *
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii}
 * @description Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
 * @description leaving only distinct numbers from the original list. Return the linked list sorted as well.
 */

/**
 * Definition for singly-linked list
 */
function ListNode(val, next) {
  this.val = (val === undefined ? 0 : val)
  this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const deleteDuplicates = function (head) {
  // return if list has 1 or no node
  if (!head || !head.next) return head;

  let duplicate = null;
  let unique = null;
  let result = null;
  while (head) {
    // check duplicacy with previous value and next node's value
    if (head.val !== duplicate) {
      if ((head.next && head.next.val !== head.val) || head.next === null) {
        // create new node and add the node at head
        unique = new ListNode(head.val, unique)
      }
    }

    duplicate = head.val;
    head = head.next;
  }

  // reverse the list
  while (unique) {
    let temp = unique.next;
    unique.next = result;
    result = unique;
    unique = temp;
  }

  return result;
};