# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.symmetric(root.left, root.right)
        
    def symmetric(self, sub1, sub2) -> bool:
        if sub1 == None or sub2 == None:
            return sub1 == sub2
        
        if sub1.val != sub2.val:
            return False
        
        return (self.symmetric(sub1.left, sub2.right) and self.symmetric(sub1.right, sub2.left) )
        
        
        
        