/**
 * [Problem ref]{@link  https://leetcode.com/problems/find-bottom-left-tree-value/}
 * @description Given the root of a binary tree, return the leftmost value in the last row of the tree.
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
const findBottomLeftValue = function (root) {
  let deepest_row = Number.NEGATIVE_INFINITY;
  let value;

  function traverse(root, level) {
    if (!root) {
      return null;
    }

    // go to left sub tree
    traverse(root.left, level + 1);

    //  check if it is the deepest level or not,if yes then
    // keep the left most leaf node's value as the current left most value
    if (level > deepest_row) {
      deepest_row = level;
      value = root.value
    }

    // go to right sub tree
    traverse(root.right, level + 1);
  }

  traverse(root, 0);

  return value;
};