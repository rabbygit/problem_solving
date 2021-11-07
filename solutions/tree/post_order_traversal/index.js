/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/binary-tree-postorder-traversal/}
 * @description Given the root of a binary tree, return the postorder traversal of its nodes' values.
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
 * @description post order(left-right-root) taversal with recursion
 * @param {TreeNode} root
 * @return {number[]}
 */
const postorderTraversal = function (root) {
  const result = [];

  if (!root) return result;

  function traverse(root) {
    if (!root) return;

    traverse(root.left); // traverse left sub tree

    traverse(root.right); // traverse right sub tree

    result.push(root.val); // push root value to result array
  }

  traverse(root);

  return result;
};

/**
 * @description post order(left-right-root) taversal without recursion
 * @param {TreeNode} root
 * @return {number[]}
 */
const postorderTraversalWithStack = function (root) {
  const result = [];
  const stack = [];

  if (!root) return result;

  stack.push(root) // push the root

  // pre order(root-left_right) traverse actually!
  while (stack.length) {
    const node = stack.pop()
    if (node) {
      if (node.left) {
        stack.push(node.left)
      }

      if (node.right) {
        stack.push(node.right)
      }

      result.push(node.val)
    }
  }

  // reverse pre order result
  // result is now in post order(left - right - root)!
  return result.reverse()
};