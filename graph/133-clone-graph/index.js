/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

function Node(val, neighbors) {
  this.val = val === undefined ? 0 : val;
  this.neighbors = neighbors === undefined ? [] : neighbors;
}

/**
 * @param {Node} node
 * @return {Node}
 */
const cloneGraph = function (node) {
  if (!node) return node;

  const nodeMap = new Map();

  function clone(node) {
    if (nodeMap.has(node)) {
      return nodeMap.get(node);
    }

    const copy = new Node(node.val);
    nodeMap.set(node, copy);

    for (const nei of node.neighbors) {
      copy.neighbors.push(clone(nei));
    }

    return copy;
  }

  return clone(node);
};
