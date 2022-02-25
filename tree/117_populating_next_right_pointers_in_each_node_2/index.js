/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/}
 * @description Populate each next pointer to point to its next right node. 
 * If there is no next right node, the next pointer should be set to NULL.
 * Initially, all next pointers are set to NULL
*/

/**
 * 
 * Follow-up:
 * 1. You may only use constant extra space.
 * 2. The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
*/

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
    if (!root) return root;

    let node = root

    while (node) {
        let dummy = new Node(0) // track the upper level's parent node
        let temp = dummy // to connect the same level's nodes

        while (node) {
            // if this node has left child, we will connect with temp
            if (node.left) {
                temp.next = node.left
                temp = temp.next
            }

            // if this node has right child, we will connect with temp
            if (node.right) {
                temp.next = node.right
                temp = temp.next
            }

            // update current level's next node, since the right most node points to null
            node = node.next
        }

        // move to the next level with dummy node which is pointing to the start of previous level
        node = dummy.next
    }

    return root
};