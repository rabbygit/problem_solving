/**
 * [Problem ref]{@link  https://leetcode.com/problems/copy-list-with-random-pointer/description/}
 *
 */

/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
const copyRandomList = function (head) {
  const nodeMap = new Map();
  nodeMap.set(null, null);

  let curr = head;
  while (curr) {
    nodeMap.set(curr, new Node(curr.val));
    curr = curr.next;
  }

  curr = head;
  while (curr) {
    const copyNode = nodeMap.get(curr);
    copyNode.next = nodeMap.get(curr.next);
    copyNode.random = nodeMap.get(curr.random);
    curr = curr.next;
  }

  return nodeMap.get(head);
};
