/**
 * [Problem ref]{@link  https://leetcode.com/problems/invert-binary-tree/description/}
 * @description Given the root of a binary tree, invert the tree, and return its root.
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
 * @return {TreeNode}
 */
const invertTree = function (root) {
  if (!root) {
    return null;
  }

  const inverted = new TreeNode(root.val);
  inverted.right = invertTree(root.left);
  inverted.left = invertTree(root.right);

  return inverted;
};
