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
  let small_num;
  let big_num;

  if (p.val > q.val) {
    big_num = p.val
    small_num = q.val
  } else {
    big_num = q.val
    small_num = p.val
  }

  if (root.val === small_num || root.val === big_num) {
    return root;
  }

  function findAnchestor(root) {
    if (root.val === small_num || root.val === big_num) {
      return true
    }

    let left = null
    let right = null
    if (root.left && root.val > small_num) {
      left =  findAnchestor(root.left)
    }

    if (root.right) {
      right = findAnchestor(root.right)
    }

    return 
  }
};