/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/flatten-binary-tree-to-linked-list/}
 * @description Given the root of a binary tree, flatten the tree into a "linked list":
 * 1. The "linked list" should use the same TreeNode class 
 * where the right child pointer points to the next node in the list and
 * the left child pointer is always null.
 * 
 * 2. The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
const flatten = function (root) {
  function traverse(node) {
    if (!node) return

    // move to left
    traverse(node.left)
    
    // if left sub tree has any node,we will move this node to right sub tree
    if(node.left){
      // keep track the current right node
      let temp =  node.right

      // move the left node to right and mark left as null
      node.right = node.left
      node.left  = null

      // keep the current right node to the end of new right sub tree
      let t = node.right
      while (t.right) {
        t = t.right
      }
      t.right = temp
    }

    traverse(node.right)
  }

  traverse(root)
};