# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.min = float("inf")
        self.previous = None

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.min

    def dfs(self, root):
        if root == None:
            return

        self.dfs(root.left)

        if self.previous != None:
            self.min = min(self.min, abs(root.val - self.previous.val))
        
        # update the previous with current node
        self.previous = root
        
        self.dfs(root.right)



            