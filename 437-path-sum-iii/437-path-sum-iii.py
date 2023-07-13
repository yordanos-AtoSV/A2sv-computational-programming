# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def pathsum(root, targetSum):
            if root == None:
                return 0
            
            res  = 0
            if root.val == targetSum:
                res += 1
                
            res += pathsum(root.left, targetSum - root.val)
            res += pathsum(root.right, targetSum - root.val) 
            return res
        
        if root == None:
            return 0
        
        return self.pathSum(root.left, targetSum) + pathsum(root, targetSum) + self.pathSum(root.right, targetSum)