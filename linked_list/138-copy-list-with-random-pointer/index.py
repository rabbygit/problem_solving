"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {None: None}  # map old to new node

        current = head
        while current:
            nodeMap[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            copyNode = nodeMap[current]
            copyNode.next = nodeMap[current.next]
            copyNode.random = nodeMap[current.random]
            current = current.next

        return nodeMap[head]
