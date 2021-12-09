/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/sum-root-to-leaf-numbers/}
 * @description You are given the root of a binary tree containing digits from 0 to 9 only.
 * Each root-to-leaf path in the tree represents a number.
 * For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
 * Return the total sum of all root-to-leaf numbers. 
 * Test cases are generated so that the answer will fit in a 32-bit integer.
 * A leaf node is a node with no children.
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
const sumNumbers = function (root) {
  let sum = 0;

  function sumOfLeaf(root, prev_root_track) {
    // return since it's the end of one path
    if (!root) return null;

    // add the node to traversed path
    prev_root_track += `${root.val}`;

    // move to left
    sumOfLeaf(root.left, prev_root_track);

    // determine leaf node
    if (!root.left && !root.right) {
      // add to sum the traversed path from root
      sum += Number(prev_root_track);
    }

    // move to right
    sumOfLeaf(root.right, prev_root_track);
  }

  sumOfLeaf(root, '');

  return sum;
};