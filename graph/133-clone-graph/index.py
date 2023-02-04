"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloneMap = {}

        def dfs(node):
            if node in cloneMap:
                return cloneMap[node]

            copyNode = Node(node.val)
            cloneMap[node] = copyNode

            for neighbor in node.neighbors:
                copyNode.neighbors.append(dfs(neighbor))

            return copyNode

        return dfs(node)