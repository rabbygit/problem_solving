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
 * @param {number[]} postorder
 * @return {TreeNode}
 */
const constructFromPrePost = function (preorder, postorder) {
  if (!preorder.length || !postorder.length) {
    return null;
  }

  // construct the root from the first element of the preorder array
  let root = new TreeNode(preorder[0]);

  // find the root value from postorder
  const index = postorder.findIndex(element => element === preorder[1]);

  // construct the left sub tree
  root.left = constructFromPrePost(preorder.slice(1, index + 2), postorder.slice(0, index + 1));
  // construct the right sub tree
  root.right = constructFromPrePost(preorder.slice(index + 2), postorder.slice(index + 1, postorder.length - 1))

  // return the root
  return root;
};