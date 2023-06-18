/**
 * [Problem ref]{@link https://leetcode.com/problems/path-sum/}
 * @description Given the root of a binary tree and an integer targetSum,
 * return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
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
 * @param {number} targetSum
 * @return {boolean}
 */
const hasPathSum = function (root, targetSum) {
  function dfs(node, sum) {
    if (!node) {
      return false;
    }

    // add the node value to sum
    sum += node.val;

    // check if node is leaf node(no child node) and sum is equal to targetSum
    if (!node.left && !node.right) {
      return sum === targetSum;
    }

    return dfs(node.left, sum) || dfs(node.right, sum);
  }

  return dfs(root, 0);
};
