# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
      sum = 0

      def sumOfLeaf(root,prev_root_track):
        nonlocal sum
        
        if not root:
          return None

        prev_root_track = prev_root_track + str(root.val)

        sumOfLeaf(root.left,prev_root_track)

        if not root.left and not root.right:
          sum += int(prev_root_track)

        sumOfLeaf(root.right,prev_root_track)

      sumOfLeaf(root,'')

      return sum