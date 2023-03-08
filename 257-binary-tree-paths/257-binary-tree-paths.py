# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        values = []
        self.path = []
        self.traverse(root, values)
        return self.path
        
    def traverse(self, root, values):
        if not root:
            return 
        if not root.left and not root.right:
            values.append(str(root.val))
            self.path.append("->".join(values))
            return 
        
        
        self.traverse(root.left, values + [str(root.val)] )
        self.traverse(root.right, values + [str(root.val)] )
        
        