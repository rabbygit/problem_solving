/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/binary-search-tree-iterator/}
 * @description Implement the BSTIterator class that 
 * represents an iterator over the in-order traversal of a binary search tree (BST):
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
 * @description Runtime for next and hasNext() is O(1) and space is O(n) number of nodes
 * @param {TreeNode} root
 */
const BSTIterator = function (root) {
    this.stack = []
    this.constructStack(root)
};

BSTIterator.prototype.constructStack = function (root) {
    if (!root) return

    this.constructStack(root.right)
    this.stack.push(root.val)
    this.constructStack(root.left)
    
};

/**
 * @return {number}
 */
BSTIterator.prototype.next = function () {
    return this.stack.pop()
};

/**
 * @return {boolean}
 */
BSTIterator.prototype.hasNext = function () {
    return !!this.stack.length
};


//////////////////////////////////////////

/**
 * @description Runtime for next and hasNext() is avg O(1) and space is O(h) height of the tree
 * @param {TreeNode} root
 */
 const BSTIterator = function (root) {
    this.stack = []
    this.constructStack(root)
};

BSTIterator.prototype.constructStack = function (node) {
   // add left child as far as it has
    while (node) {
       this.stack.push(node)
       node = node.left
   } 
};

/**
 * @return {number}
 */
BSTIterator.prototype.next = function () {
    const node = this.stack.pop()
    
    // add right child if has any
    if (node.right)  this.constructStack(node.right)

    return node.val
};

/**
 * @return {boolean}
 */
BSTIterator.prototype.hasNext = function () {
    return !!this.stack.length
};