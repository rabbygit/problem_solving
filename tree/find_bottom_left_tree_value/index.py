# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        value = 0
        deepest_row = float('-inf')
        
        def traverse(root,level):
          
          nonlocal value
          nonlocal deepest_row
          
          if not root:
            return None
          
          # move left
          traverse(root.left,level+1)
        
          
          if level > deepest_row:
            deepest_row = level
            value = root.val

          # move right
          traverse(root.right,level+1)
          
          
        traverse(root,0)

        return value