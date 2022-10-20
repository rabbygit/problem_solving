/**
 * [Problem ref]{@link  https://leetcode.com/problems/merge-two-binary-trees/}
 * @description You are given two binary trees root1 and root2.
 * Imagine that when you put one of them to cover the other, 
 * some nodes of the two trees are overlapped while the others are not. 
 * You need to merge the two trees into a new binary tree. 
 * The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
 * Otherwise, the NOT null node will be used as the node of the new tree.
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
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */
const mergeTrees = function (root1, root2) {
    function merge(node1, node2, prev, call) {
        if (!node1 && !node2) return

        if (node1 && node2) {
            // overlap and sum value
            node2.val = node1.val + node2.val
        } else if (node1 && prev) {
            // left root has value but right root doesn't have, in that case we have to
            // add the left root to result tree's left or right
            // if it is call for left sub tree than add as left child otherwise right child
            if (!prev.left && call == 'l') prev.left = node1
            else prev.right = node1
        }

        prev = node2

        merge(node1 ? node1.left : null, node2 ? node2.left : null, prev , 'l')
        merge(node1 ? node1.right : null, node2 ? node2.right : null, prev , 'r')
    }

    merge(root1, root2, root2)

    return root2 ? root2 : root1
};