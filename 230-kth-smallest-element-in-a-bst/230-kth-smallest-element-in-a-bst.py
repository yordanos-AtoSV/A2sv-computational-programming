# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def recur(root):
            if not root :
                return 
            
            
            recur(root.left)
            self.arr.append(root.val)
            recur(root.right)
        
        
        self.arr = []
        recur(root)
        return self.arr[k - 1]
        
       
            
            
        