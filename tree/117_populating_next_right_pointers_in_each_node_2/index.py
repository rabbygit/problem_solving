"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root

        while(node):
            dummy = Node(0) # track the upper level's parent node
            temp = dummy # to connect the same level's nodes

            while(node):
                # if this node has left child, we will connect with temp
                if node.left is not None:
                    temp.next = node.left
                    temp = temp.next

                # if this node has right child, we will connect with temp
                if node.right is not None:
                    temp.next = node.right
                    temp = temp.next
                
                # update current level's next node, since the right most node points to null
                node = node.next
            
            # move to the next level with dummy node which is pointing to the start of previous level
            node = dummy.next

        return root