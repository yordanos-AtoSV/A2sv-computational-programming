# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        
        def dp(node):
            
            if not node:
                return 0
            temp = temp2 = 0
            if node not in memo:
                if node.left:
                    temp = dp(node.left.left) + dp(node.left.right)
                if node.right:
                    temp2 = dp(node.right.left) + dp(node.right.right)
                    
                pick = node.val + temp + temp2
                
                notpick = dp(node.left) + dp(node.right)
                
                memo[node] = max(pick, notpick)
                
                
            return memo[node]
        
        
        return dp(root)