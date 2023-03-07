# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.inorderTraverse(root)
        return self.ans
        
    def inorderTraverse(self, root: Optional[TreeNode]):
            if not root :
                return
        
            self.inorderTraverse(root.left)
            self.ans.append(root.val)
            self.inorderTraverse(root.right)
    
            
            
        
        