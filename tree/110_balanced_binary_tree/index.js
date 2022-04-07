/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/balanced-binary-tree/}
 * @description Given a binary tree, determine if it is height-balanced.
 * For this problem, a height-balanced binary tree is defined as:
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
 * @return {boolean}
 */
const isBalanced = function (root) {
  if (!root) return true

  function maxDepth(node) {
    if (!node) return -1

    let left_depth = maxDepth(node.left)
    let right_depth = maxDepth(node.right)

    return Math.max(left_depth, right_depth) + 1
  }

  return Math.abs(maxDepth(root.left) - maxDepth(root.right)) < 2
};


const root = {
  val: 1,
  left: null,
  right: {
    val: 1,
    left: null,
    right: null
  }
}

console.log(isBalanced(root))