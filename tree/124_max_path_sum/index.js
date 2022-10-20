/**
 * [Problem ref]{@link  https://leetcode.com/problems/binary-tree-maximum-path-sum/}
 * @description A path in a binary tree is a sequence of nodes where
 * each pair of adjacent nodes in the sequence has an edge connecting them.
 * A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
 * The path sum of a path is the sum of the node's values in the path.
 * Given the root of a binary tree, return the maximum path sum of any non-empty path.
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
const maxPathSum = function (root) {
    let mps = Number.NEGATIVE_INFINITY;

    function findMax(root) {
        if (!root) {
            return 0;
        }

        // choose the higest value of left sub-tree
        let lps = Math.max(0, findMax(root.left));
        // choose the higest value of right sub-tree
        let rps = Math.max(0, findMax(root.right));
        // keep track of the higest value,after comparing the previous highest value with
        // combined value of current left , right and root
        mps = Math.max(mps, lps + root.val + rps);

        // propagate root+left or root+right nodes value to compare in upper level
        return root.val + Math.max(lps, rps);
    }

    findMax(root);

    return mps;
};

