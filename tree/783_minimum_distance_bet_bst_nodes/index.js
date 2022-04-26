/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/minimum-distance-between-bst-nodes/}
 * @description Given the root of a Binary Search Tree (BST), 
 * return the minimum difference between the values of any two different nodes in the tree.
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
const minDiffInBST = function (root) {
    let min = Number.POSITIVE_INFINITY
    let previous = null

    function dfs(root) {
        if(!root) return;

        dfs(root.left)

        if (previous) {
            min = Math.min(min, Math.abs(previous.val - root.val))
        }

        // update the previous
        previous = root

        dfs(root.right)
    }

    dfs(root)
    return min;
};