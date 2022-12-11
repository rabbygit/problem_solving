/**
 * [Problem ref]{@link  https://leetcode.com/problems/count-good-nodes-in-binary-tree}
 * @description Given a binary tree root, a node X in the tree is named good
 * if in the path from root to X there are no nodes with a value greater than X.
 * Return the number of good nodes in the binary tree.
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
const goodNodes = function (root) {
  let total_good = 0;

  function dfs(root, currMax) {
    if (!root) return;

    if (root.val >= currMax) {
      total_good++;
      currMax = root.val;
    }

    dfs(root.left, currMax);
    dfs(root.right, currMax);
  }

  dfs(root, root.val);
  return total_good;
};
