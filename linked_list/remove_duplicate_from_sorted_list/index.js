/**
 *
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/remove-duplicates-from-sorted-list/}
 * @description Remove Duplicates from Sorted List
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
  let track_node = null;
  let reverse = null

  while (head) {
    // check unique value and add it to head
    if (!track_node || track_node.val !== head.val) {
      track_node = new ListNode(head.val, track_node);
    }
    head = head.next;
  }

  // reverse the list
  while (track_node) {
    let temp = track_node.next;
    track_node.next = reverse;
    reverse = track_node
    track_node = temp
  }
  return reverse;
};