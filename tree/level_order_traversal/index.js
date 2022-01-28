/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/binary-tree-level-order-traversal/}
 * @description Given the root of a binary tree, 
 * return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
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
const levelOrder = function (root) {
    let result = [];
    let level_list = {};
    if (!root) return result;

    // traverse tree and keep track of level
    function traverse(root, level) {
        // if root is null then return
        if (!root) return;
        // go left and increase level by 1
        traverse(root.left, level + 1);
        // check if the level is already visited or not
        // if visited the push the root value to level's node
        // else create key as level number and push root value
        if (level_list[level]) {
            level_list[level].nodes.push(root.val);
        } else {
            level_list[level] = {
                nodes: [root.val]
            }
        }
        // go right and increase level by 1
        traverse(root.right, level + 1);
    }

    // call traverse from level 0
    traverse(root, 0)

    // loop through each level as key
    // push node's list to result array
    for (const key in level_list) {
        if (Object.hasOwnProperty.call(level_list, key)) {
            const element = level_list[key];
            result.push(element.nodes)
        }
    }

    return result;
};