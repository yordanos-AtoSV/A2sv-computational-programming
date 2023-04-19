# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node,parent, path):
            nonlocal ans 
            if parent:
                if not parent.left and not parent.right:
                    sum = "".join(map(str,path))
                    ans += int(sum)
                    return 
            if node:
                path.append(node.val)
                dfs(node.left,node, path)
                dfs(node.right,node, path)
                path.pop()
            
            
        dfs(root,None, [])
        return ans // 2
        