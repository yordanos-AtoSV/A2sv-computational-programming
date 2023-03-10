# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recur(root, left, right):
            
            if not root:
                return True

            if not(root.val > left and root.val < right):
                return False
            
            return (recur(root.left, left, root.val) and recur(root.right, root.val, right))
        
        return (recur(root, float("-inf"), float("inf")))
        
