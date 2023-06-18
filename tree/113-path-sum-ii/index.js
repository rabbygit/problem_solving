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
 * @return {number[][]}
 */
const pathSum = function (root, targetSum) {
  const result = [];

  function possiblePath(node, sum, sub_result) {
    if (!node) return;

    sum += node.val;
    sub_result.push(node.val);

    // check if it is leaf node and
    // targetSum is equal to the sum upto this node
    if (!node.left && !node.right && targetSum === sum) {
      result.push([...sub_result]);
    }

    possiblePath(node.left, sum, sub_result);
    possiblePath(node.right, sum, sub_result);

    sub_result.pop();
  }

  possiblePath(root, 0, []);

  return result;
};
