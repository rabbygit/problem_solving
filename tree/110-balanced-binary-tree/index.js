/**
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
 * @description run time O(n log n)
 * @param {TreeNode} root
 * @return {boolean}
 */
const isBalanced = function (root) {
  let balanced = true;

  function findMaxHeight(root) {
    if (!root) return 0;

    const leftMax = findMaxHeight(root.left);
    const rightMax = findMaxHeight(root.right);
    
    const diff = Math.abs(leftMax - rightMax);
    balanced = balanced && diff <= 1;

    return 1 + Math.max(leftMax, rightMax);
  }

  findMaxHeight(root);
  return balanced;
};
