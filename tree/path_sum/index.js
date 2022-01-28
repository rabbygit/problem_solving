/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/path-sum/}
 * @description Given the root of a binary tree and an integer targetSum, 
 * return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
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
 * @param {number} targetSum
 * @return {boolean}
 */
const hasPathSum = function (root, targetSum) {
    let result = false;
    if (!root) return result;

    function traverse(root, sum) {
        if (!root) return;

        // add the root value to sum
        sum += root.val;

        // move left
        traverse(root.left, sum);

        // check if root is leaf node(no child node) and sum is equal to targetSum
        if (!root.left && !root.right && (sum === targetSum)) {
            result = true;
        }

        // move right
        traverse(root.right, sum)
    }

    traverse(root, 0)

    return result;
};