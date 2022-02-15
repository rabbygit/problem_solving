/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/flatten-binary-tree-to-linked-list/}
 * @description Given the root of a binary tree, flatten the tree into a "linked list":
 * 1. The "linked list" should use the same TreeNode class 
 * where the right child pointer points to the next node in the list and
 * the left child pointer is always null.
 * 
 * 2. The "linked list" should be in the same order as a pre-order traversal of the binary tree.
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
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
const flatten = function (root) {
  const linked_list = new List()

  function traverse(node) {
    if (!node) return

    // add the node to linked list
    linked_list.add(node.val)

    traverse(node.left)
    traverse(node.right)
  }

  traverse(root)

  return linked_list.returnHead()
};

class TreeNode {
  constructor(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
  }
}

class List {
  constructor() {
    this.head = null
    this.tail = null
  }

  add(value) {
    const node = new TreeNode(value, null, null)
    if (!this.head) {
      this.head = this.tail = node
      return
    }

    // add to tail
    this.tail.right = node
    this.tail = node
  }

  returnHead() {
    return this.head
  }
}

const root = {
  val: 1,
  left: {
    val: 2,
    left: {
      val: 3,
      left: null,
      right: null
    },
    right: null
  },
  right: {
    val: 5,
    left: null,
    right: {
      val: 6,
      left: null,
      right: null
    }
  }
}

console.log(flatten(root));