/**
 * [Problem ref]{@link  https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/}
 * @description Given two integer arrays preorder and inorder 
 * where preorder is the preorder traversal of a binary tree and 
 * inorder is the inorder traversal of the same tree,
 * construct and return the binary tree.
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
const buildTree = function (preorder, inorder) {
    if (!preorder.length || !inorder.length) {
        return null;
    }

    // construct the root from the first element of the preorder array
    let root = new TreeNode(preorder[0]);
    // find the root value from inorder
    let index = inorder.findIndex(element => element === preorder[0])

    // construct the left sub tree
    root.left = buildTree(preorder.slice(1, index + 1), inorder.slice(0, index + 1))
    // construct the right sub tree
    root.right = buildTree(preorder.slice(index + 1), inorder.slice(index + 1))

    // return the root
    return root;
};