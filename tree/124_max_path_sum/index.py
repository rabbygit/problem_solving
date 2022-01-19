# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mps = float("-inf")
        
        def findMax(root):
          nonlocal mps
          
          if not root:
            return 0
          
          lps = max(0,findMax(root.left))
          rps = max(0,findMax(root.right))
          
          mps = max(mps, lps+root.val+rps)
          
          return root.val + max(lps,rps)
        
        findMax(root)
        
        return mps