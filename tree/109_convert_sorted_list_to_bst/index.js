/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/}
 * @description Given the head of a singly linked list where elements are sorted in ascending order,
 * convert it to a height balanced BST.For this problem,
 * a height-balanced binary tree is defined as a binary tree in which
 * the depth of the two subtrees of every node never differ by more than 1.
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
function TreeNode(val, left, right) {
  this.val = (val === undefined ? 0 : val)
  this.left = (left === undefined ? null : left)
  this.right = (right === undefined ? null : right)
}
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
const sortedListToBST = function (head) {
  let length = 0
  let index_map = {}

  // Find total length of the list and map each node's value to index no
  let node = head
  while (node) {
    index_map[length++] = node.val
    node = node.next
  }

  // construct the tree recursively
  function constructBST(left, right) {
    if (left > right) {
      return null
    }

    let mid = parseInt((left + right) / 2)
    let root = new TreeNode(index_map[mid])

    root.left = constructBST(left, mid - 1)
    root.right = constructBST(mid + 1, right)

    return root
  }

  return constructBST(0, length - 1)
};