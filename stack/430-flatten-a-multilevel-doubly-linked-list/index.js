/**
 * // Definition for a Node.
 * function Node(val,prev,next,child) {
 *    this.val = val;
 *    this.prev = prev;
 *    this.next = next;
 *    this.child = child;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
const flatten = function (head) {
  if (!head) return head;

  let dummy = new Node(0, null, null, null);
  let curr = dummy;
  const stack = [head];

  while (stack.length) {
    const tmp = stack.pop();
    if (tmp.next) stack.push(tmp.next);
    if (tmp.child) stack.push(tmp.child);
    curr.next = tmp;
    tmp.prev = curr;
    tmp.child = null;
    curr = tmp;
  }

  dummy.next.prev = null;
  return dummy.next;
};
