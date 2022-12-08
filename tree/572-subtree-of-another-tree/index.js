/**
 * [Problem ref]{@link  https://leetcode.com/problems/same-tree/}
 * @description Given the roots of two binary trees p and q,
 *  write a function to check if they are the same or not.
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
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
const isSameTree = function (p, q) {
  // if code reaches this point,
  // it means both are equal
  if (!p && !q) return true;

  // mismatch
  if (!p || !q) return false;

  // mismatch
  if (p.val != q.val) return false;

  // recursively call the left and right of the tree
  // compare and return boolean result to previous stack call
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
const isSubtree = function (root, subRoot) {
  // if both tree is null or the subRoot is null we can say subtree exists in the root tree
  // if tree is null but subRoot is not null then subtree doesn't exist in the root tree
  if (subRoot === null) {
    return true;
  }
  if (root === null) {
    return false;
  }

  if (isSameTree(root, subRoot)) {
    return true;
  }

  // recursively check for left and right subtree if they are same tree
  // time complexit: O(root * subRoot)
  return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};
