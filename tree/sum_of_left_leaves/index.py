# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0
        
        def traverse(root , column , prev):
            nonlocal sum
            
            if not root:
                return None
            
            traverse(root.left , column-1 , column)
            
            # check if it is left and leaf node
            if not root.left and not root.right and prev - 1 == column:
                sum += root.val
                
            traverse(root.right , column+1 , column)
            
            
        traverse(root,0,0)
            
        
        return sum