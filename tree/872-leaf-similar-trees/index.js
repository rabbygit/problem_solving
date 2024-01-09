/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
const leafSimilar = function (root1, root2) {
  const leafValues1 = [];
  const leafValues2 = [];

  getLeafValues(root1, leafValues1);
  getLeafValues(root2, leafValues2);

  return (
    leafValues1.length === leafValues2.length &&
    leafValues1.every((value, index) => value === leafValues2[index])
  );
};

function getLeafValues(node, leafValues) {
  if (!node) return;

  if (!node.left && !node.right) {
    leafValues.push(node.val);
    return;
  }

  getLeafValues(node.left, leafValues);
  getLeafValues(node.right, leafValues);
}
