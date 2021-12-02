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
const sumOfLeftLeaves = function (root) {
  let sum = 0;
  let deepest_row = Number.NEGATIVE_INFINITY;

  if (!root.left) {
    return sum;
  }

  function traverse(root, level, column, prev) {
    if (!root) {
      return null;
    }


    traverse(root.left, level + 1, column - 1, column)

    if (!root.left && !root.right && level > deepest_row && prev < column - 1) {
      deepest_row = level
      sum += root.val;
    }

    traverse(root.right, level + 1, column + 1, column)
  }

  traverse(root, 0, 0, 0);

  return sum;
};

