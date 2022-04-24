/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/leaf-similar-trees/}
 * @description Consider all the leaves of a binary tree, from left to right order, 
 * the values of those leaves form a leaf value sequence
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
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
const leafSimilar = function (root1, root2) {
  let root1_leaf = leafNodes(root1)
  let root2_leaf = leafNodes(root2)

  if (root1_leaf.length !== root2_leaf.length) {
    return false
  }

  // compare the two array
  for (let index = 0; index < root1_leaf.length; index++) {
    if (root1_leaf[index] !== root2_leaf[index]) {
      return false
    }
  }

  return true
};

function leafNodes(root) {
  let list = []

  if (!root) return list

  if (!root.left && !root.right) {
    list.push(root.val)
    return list
  }

  let l_nodes = leafNodes(root.left)
  let r_nodes = leafNodes(root.right)

  list.push(...l_nodes, ...r_nodes)

  return list
}