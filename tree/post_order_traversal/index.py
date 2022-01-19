# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        def traverse(root):
            if not root:
                return 
            
            # traverse left sub tree 
            traverse(root.left)
            
            # traverse right sub tree
            traverse(root.right)
            
            # append the root
            result.append(root.val)
            
        traverse(root)
        
        return result

    # solution without recursion
    def postorderTraversalWithStack(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        stack = []
        if not root:
            return result
        
        stack.append(root)
        
        # pre order(root-left_right) traverse actually!
        while len(stack):
            
            node = stack.pop()

            if node.left is not None:
                stack.append(node.left)
                
            if node.right is not None:
                stack.append(node.right)
          
                
            result.append(node.val)
        
        # reverse pre order result
        # result is now in post order(left-right-root)!
        result.reverse()
        
        return result
        