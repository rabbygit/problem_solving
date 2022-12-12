/**
 * [Problem ref]{@link  https://leetcode.com/problems/kth-smallest-element-in-a-bst}
 * @description Given the root of a binary search tree, and an integer k,
 * return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
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
 * @param {number} k
 * @return {number}
 */
const kthSmallest = function (root, k) {
  let n = 0;
  let current = root;
  const stack = [];

  // in-order traversal(left-root-right)
  while (current || stack.length) {
    while (current) {
      stack.push(current);
      current = current.left;
    }

    current = stack.pop();
    n++;

    if (n === k) {
      return current.val;
    }

    current = current.right;
  }
};
