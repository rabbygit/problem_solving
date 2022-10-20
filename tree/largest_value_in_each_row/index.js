/**
 * [Problem ref]{@link  https://leetcode.com/problems/find-largest-value-in-each-tree-row/}
 * @description Given the root of a binary tree, 
 *  return an array of the largest value in each row of the tree (0-indexed).
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
 * @return {number[]}
 */
const largestValues = function (root) {
  let result = [];
  let level_list = {};
  if (!root) return result;

  // traverse tree and keep track of level's max value
  function traverse(root, level) {
    if (!root) return;

    // move left
    traverse(root.left, level + 1);

    // if root's value is the first for the level or has max value than current level's value
    // then replace with current root value
    if (level_list[level] === undefined || level_list[level] < root.val) {
      level_list[level] = root.val;
    }

    // move right
    traverse(root.right, level + 1);
  }

  traverse(root, 0);

  for (let level = 0; level < Object.keys(level_list).length; level++) {
    result.push(level_list[level]);
  }

  return result;
};