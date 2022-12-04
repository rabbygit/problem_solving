/**
 * [Problem ref]{@link  https://leetcode.com/problems/diameter-of-binary-tree/}
 * @description Given the root of a binary tree, return the length of the diameter of the tree.
 * The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
 * This path may or may not pass through the root.
 * The length of a path between two nodes is represented by the number of edges between them.
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
 * @return {number}
 */
const diameterOfBinaryTree = function (root) {
  let diameter = Number.NEGATIVE_INFINITY;

  function findMax(root) {
    if (!root) return 0;

    // choose the higest diamete of left sub-tree
    let leftMax = findMax(root.left);
    // choose the higest diamete of right sub-tree
    let rightMax = findMax(root.right);
    // keep track of the higest diamete, after comparing the previous highest diamete with
    // combined value of current left , right
    diameter = Math.max(diameter, leftMax + rightMax);

    // propagate root+left or root+right nodes value to compare in upper stack call
    return 1 + Math.max(leftMax, rightMax);
  }

  findMax(root);

  return diameter;
};
