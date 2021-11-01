# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        level_list = {}
        
        if not root:
            return result
        
        
        def traverse(root,level):
            if not root:
                return
            
            traverse(root.left,level+1)
            
            if str(level) in level_list:
                level_list[str(level)].append(root.val)
                
            else:
                level_list[str(level)] = [root.val]
                
            
            traverse(root.right,level+1)
            
        
        traverse(root,0)
        
        for level in range(len(level_list)):
            if str(level) in level_list:
                result.append(level_list[str(level)])
                
        
        return result