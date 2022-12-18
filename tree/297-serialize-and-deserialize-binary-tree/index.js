/**
 * [Problem ref]{@link  https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/}
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
const serialize = function (root) {
  const serialized = [];

  function dfs(node) {
    if (!node) {
      serialized.push("N");
      return;
    }

    serialized.push(String(node.val));
    dfs(node.left);
    dfs(node.right);
  }

  dfs(root);
  return serialized.join(",");
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
const deserialize = function (data) {
  let i = 0;
  const nodes = data.split(",");

  function dfs() {
    if (nodes[i] === "N") {
      i++;
      return null;
    }

    const root = new TreeNode(Number(nodes[i]));
    i++;
    root.left = dfs();
    root.right = dfs();

    return root;
  }

  return dfs();
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
