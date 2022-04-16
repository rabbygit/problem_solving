/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/unique-binary-search-trees-ii/}
 * @description Given an integer n, return all the structurally unique BST's (binary search trees), 
 * which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
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
 * @param {number} n
 * @return {TreeNode[]}
 */
const generateTrees = function (n) {
    function constructBST(start, end) {
        let list = []
        if (start > end) {
            list.push(null)
            return list
        }

        for (let index = start; index <= end; index++) {
            let left_trees = constructBST(start, index - 1)
            let right_trees = constructBST(index + 1, end)

            for (const left_tree of left_trees) {
                for (const right_tree of right_trees) {
                    const node = new TreeNode(index)
                    node.left = left_tree
                    node.right = right_tree
                    list.push(node)
                }
            }
        }

        return list
    }

    return constructBST(1, n)
};