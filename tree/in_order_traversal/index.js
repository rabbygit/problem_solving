/**
 * [Problem ref]{@link  https://leetcode.com/problems/binary-tree-inorder-traversal}
 * @description Given the root of a binary tree, 
 * return the inorder traversal of its nodes' values.
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
 * @return {number[]}
 */
const inorderTraversal = function (root) {
    let result = [];
    if (!root) return result;
    return traverse(root, result);
};

/**
 * @description traverse the tree in order(left-> root -> right)
 * @param {*} root 
 * @param {*} result 
 * @returns {number[]}
 */
const traverse = (root, result) => {
    // if root has not any node
    if (!root) return;

    // traverse left side
    traverse(root.left, result);

    // push the root in result
    result.push(root.val);

    // traverse the right side
    traverse(root.right, result);

    // return result array
    return result;
}