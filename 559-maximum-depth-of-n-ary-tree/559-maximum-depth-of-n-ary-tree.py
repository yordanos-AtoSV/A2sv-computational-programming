"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root :
            return 0
        depth  = 0
        def dfs(node,num):
            nonlocal depth
            if not node.children:
                depth = max(num + 1, depth)
                return 
            
            for nextnode in node.children:
                dfs(nextnode, num + 1)
            
            return
                
        dfs(root, 0)
        return depth