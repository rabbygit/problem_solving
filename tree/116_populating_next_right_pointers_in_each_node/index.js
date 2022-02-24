/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {Node} root
 * @return {Node}
 */
const connect = function (root) {
  const level_list = {}
  if (!root) return root

  // traverse tree and keep track of level
  function dfs(node, level) {
    // if root is null then return
    if (!node) return;

    // go left and increase level by 1
    dfs(node.left, level + 1)

    // check if the level is already visited or not
    // if visited then update the current node's next pointer to current visiting node
    // and keep the current node as new node for the level
    // else create key as level number and keep the current node
    if (level_list[level] === undefined) {
      level_list[level] = node
    } else {
      let temp_node = level_list[level]
      temp_node.next = node
      level_list[level] = node
    }

    // go right and increase level by 1
    dfs(node.right, level + 1)
  }

  dfs(root, 0)

  return root
};