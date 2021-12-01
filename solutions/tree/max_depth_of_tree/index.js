/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/maximum-depth-of-binary-tree/}
 * @description Given the root of a binary tree, return its maximum depth.
 * A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
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
const maxDepth = function (root) {
    // if root has not any node
    if (!root) return 0;

    let depth = 1;

    // traverse tree and keep track of level
    function traverse(root, level) {
        // if root is null then return
        if (!root) return;

        // go left and increase level by 1
        traverse(root.left, level + 1);

        // check if current level is grater than depth
        if (level > depth) {
            depth = level;
        }

        // go right and increase level by 1
        traverse(root.right, level + 1);
    }

    // call traverse from level 0
    traverse(root, 1)

    return depth;
};