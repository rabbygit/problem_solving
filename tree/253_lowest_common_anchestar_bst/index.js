/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/}
 * @description Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
 * According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
 * that has both p and q as descendants (where we allow a node to be a descendant of itself).”
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
const lowestCommonAncestor = function (root, p, q) {
  let current = root;

  while (current) {
    // if both p and q's values are greater than the current node, it means need to move right sub tree
    // else to left sub tree
    // otherwise, p or q must exist in left or right subtree and this current node is the ancestor
    if (p.val > current.val && q.val > current.val) {
      current = current.right
    } else if (p.val < current.val && q.val < current.val) {
      current = current.left
    } else {
      return current
    }
  }
};