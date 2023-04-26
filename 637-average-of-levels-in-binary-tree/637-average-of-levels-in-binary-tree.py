# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:    
        def bfs(node):
        
            ans =  []
            queue = deque([node])
            
            while queue:
                n = len(queue)
                total = 0
                for i in range(n):
                    nodes = queue.popleft()
                    total += nodes.val


                    if nodes.left:
                        left = nodes.left
               
                        queue.append(left)
                    
                    if nodes.right:
                        right = nodes.right
                  
                        queue.append(right)
                        
                average = total / n 
                ans.append(average) 
                    
            return ans 

                        
                        
        return bfs(root)
        
