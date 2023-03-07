# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.height = []
        cur_sum = 0
        self.calcheight(root, cur_sum)
        return max(self.height)
    
    def calcheight(self, root: Optional[TreeNode], cur_sum):
        if not root:
            self.height.append(cur_sum)
            return
        
        self.calcheight(root.left, cur_sum + 1 )
        self.calcheight(root.right, cur_sum + 1 )
            
        