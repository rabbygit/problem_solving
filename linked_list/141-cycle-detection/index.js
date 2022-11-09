/**
 * [Problem ref]{@link  https://leetcode.com/problems/linked-list-cycle}
 * @description Given head, the head of a linked list, determine if the linked list has a cycle in it.
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 * @description with hashMap
 */
const hasCycle = function (head) {
  const nodeMap = new Map();
  let curr = head;

  while (curr) {
    if (nodeMap.get(curr)) return true;
    nodeMap.set(curr, true);
    curr = curr.next;
  }

  return false;
};

const hasCycleWithFloydCycleAlgo = function (head) {
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;

    if (slow === fast) {
      return true;
    }
  }

  return false;
};
