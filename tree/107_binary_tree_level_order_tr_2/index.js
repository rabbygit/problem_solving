/**
 * [Problem ref]{@link  https://leetcode.com/problems/binary-tree-level-order-traversal-ii/}
 * @description Given the root of a binary tree, 
 * return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
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
 * @return {number[][]}
 */
 const levelOrderBottom = function (root) {
    const level_map = {}
    const result = []

    function level_traverse(node, level) {
        if (!node) return;

        level_traverse(node.left, level + 1)

        if (level_map[level] === undefined) {
            level_map[level] = [node.val]
        }else{
            level_map[level].push(node.val)
        }

        level_traverse(node.right, level + 1)
    }

    level_traverse(root , 0)

    const length = Object.entries(level_map).length - 1

    for (let index = length; index >= 0; index--) {
       result.push([...level_map[index]])
    }

    return result
};