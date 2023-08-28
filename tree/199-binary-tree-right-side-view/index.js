/**
 * [Problem ref]{@link  https://leetcode.com/problems/binary-tree-right-side-view}
 * @description Given the root of a binary tree, imagine yourself standing on the right side of it,
 * return the values of the nodes you can see ordered from top to bottom.
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
 * @return {number[][]}
 */
const rightSideView = function (root) {
  let result = [];
  let level_list = {};

  // traverse tree and keep track of level
  function traverse(root, level) {
    // if root is null then return
    if (!root) return;
    // go left and increase level by 1
    traverse(root.left, level + 1);
    // keep the visited node,
    // incrementally, it will keep the right-most-child
    level_list[level] = root.val;
    // go right and increase level by 1
    traverse(root.right, level + 1);
  }

  // call traverse from level 0
  traverse(root, 0);

  // loop through each level as key
  // push node's list to result array
  const total_levels = Object.keys(level_list).length;
  for (let level = 0; level < total_levels; level++) {
    result.push(level_list[level]);
  }

  return result;
};
