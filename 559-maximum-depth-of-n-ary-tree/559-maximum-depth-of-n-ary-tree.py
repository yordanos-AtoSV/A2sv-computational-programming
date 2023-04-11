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
      
        def dfs(node):
         
            if not node.children:
                
                return 1
            
            temp = []    
            for nextnode in node.children:
                temp.append(dfs(nextnode))
            
            return max(temp) + 1    

                
        return dfs(root)
      