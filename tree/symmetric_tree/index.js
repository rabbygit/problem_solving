/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/symmetric-tree/}
 * @description Given the root of a binary tree,
 * check whether it is a mirror of itself (i.e., symmetric around its center).
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
 * @return {boolean}
 */
const isSymmetric = function (root) {
    return detectSymmetric(root.left, root.right);
};

function detectSymmetric(p, q) {
    if (!p && !q) return true;

    if (!p || !q) return false;

    if (p.val !== !q.val) return false;

    // compare left and right node
    // compare right and left node
    return detectSymmetric(p.left, q.right) && detectSymmetric(p.right, q.left)
}