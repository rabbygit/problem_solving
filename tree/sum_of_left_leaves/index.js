/**
 * [Problem ref]{@link  https://leetcode.com/problems/sum-of-left-leaves/}
 * @description Given the root of a binary tree, return the sum of all left leaves.
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
const sumOfLeftLeaves = function (root) {
  let sum = 0;

  // track node's column since left node always in 1 less than root's column
  function traverse(root, column, prev) {
    if (!root) return null;

    traverse(root.left, column - 1, column);

    // check leaf node and if it is the left of root
    if (!root.left && !root.right && prev - 1 === column) {
      sum += root.val;
    }

    traverse(root.right, column + 1, column);
  }

  traverse(root, 0, 0);

  return sum;
};

