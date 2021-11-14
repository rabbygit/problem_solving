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
 * @return {boolean}
 */
const hasPathSum = function (root, targetSum) {
    let result = false;

    function determinePathSum(root, sum) {
        if (!root) return;

        sum += root.val;

        determinePathSum(root.left, sum);

        if (!root.left && !root.right) {
            sum += root.val
        }
    }
};