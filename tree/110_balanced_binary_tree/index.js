/**
 * [Problem ref]{@link  https://leetcode.com/problems/balanced-binary-tree/}
 * @description Given a binary tree, determine if it is height-balanced.
 * For this problem, a height-balanced binary tree is defined as:
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
 * @description determines height of the sub-tree
 * @param {*} node 
 * @returns 
 */
function height(node) {
  if (!node) return -1

  return Math.max(height(node.left), height(node.right)) + 1
}

/**
 * @description run time O(n log n)
 * @param {TreeNode} root
 * @return {boolean}
 */
const isBalanced = function (root) {
  if (!root) return true

  let left_tree_height = height(root.left)
  let right_tree_height = height(root.right)

  let diff = Math.abs(left_tree_height - right_tree_height)

  if (diff > 1) {
    return false // propagate the result
  } else {
    // recursively check for every left and right sub-tree
    return isBalanced(root.left) && isBalanced(root.right)
  }
};



///////////////////////////////////////////////////////////////

/**
 * @description check the sub-tree when determines the height , run time O(n)
 * @param {TreeNode} root
 * @return {boolean}
 */
const checkBalance = function (root) {
  if (!root) return -1

  let left_tree_height = checkBalance(root.left)
  if (left_tree_height === Number.MIN_SAFE_INTEGER) {
    return Number.MIN_SAFE_INTEGER
  }

  let right_tree_height = checkBalance(root.right)
  if (right_tree_height === Number.MIN_SAFE_INTEGER) {
    return Number.MIN_SAFE_INTEGER
  }

  let diff = Math.abs(left_tree_height - right_tree_height)

  if (diff > 1) {
    return Number.MIN_SAFE_INTEGER // propagate the result
  } else {
    return Math.max(left_tree_height, right_tree_height) + 1
  }
};


/**
 * @param {TreeNode} root
 * @return {boolean}
 */
const isBalanced = function (root) {
  return checkBalance(root) !== Number.MIN_SAFE_INTEGER
};