# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.check = 0
        self.traverse(root)
        return self.check
    
    def traverse(self,root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.check = max(left + right, self.check)
        
        return max(left , right ) + 1
        
    

            
        