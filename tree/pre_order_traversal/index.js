/**
 * [Problem ref]{@link  https://leetcode.com/problems/binary-tree-preorder-traversal/}
 * @description Given the root of a binary tree,
 *  Given the root of a binary tree, 
 *  return the preorder traversal of its nodes' values.
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
 * @description pre_order traversal using recursion
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function (root) {
    let result = [];
    if (!root) return result;

    function traverse(root) {
        if (!root) return;

        result.push(root.val);

        traverse(root.left)
        traverse(root.right)
    }

    traverse(root)

    return result
};

/**
 * @description pre_order traversal using loop
 * @param {TreeNode} root
 * @return {number[]}
 */
const preorderTraversal = function (root) {
    let result = [];
    let stack = [];
    let runner = root;
    if (!root) return result;

    while (runner || stack.length) {

        // move left and keep track of the root to stack
        while (runner) {
            result.push(runner.val);  // push current root's val to result
            stack.push(runner); // push root to stack
            runner = runner.left; // move left
        }

        // pop the last root
        let element = stack.pop();

        // move right
        runner = element.right;
    }

    return result
};