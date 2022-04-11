# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def possiblePath(root, sum , sub_result):
            if root == None:
                return
            
            sum += root.val
            sub_result.append(root.val)

            possiblePath(root.left, sum , sub_result)

            if root.left == None and root.right == None and targetSum == sum:
                result.append(sub_result.copy())
            
            possiblePath(root.right, sum , sub_result)

            sub_result.pop()

        possiblePath(root,0,[])

        return result