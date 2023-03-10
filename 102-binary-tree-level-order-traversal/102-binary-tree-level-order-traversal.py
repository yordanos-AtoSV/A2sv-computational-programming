# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def recur(root,level):
            
            if not root:
                return
            size = len(self.ans)
            
            if size > level:
                self.ans[level].append(root.val)
            else:
                self.ans.append([root.val])
                
            recur(root.left, level + 1)
            recur(root.right, level + 1)
                
        self.ans = []   
        recur(root, 0)
        return self.ans
        
            
        