class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        suffix = [0] * (len(grid[0]) + 1)
        prefix = [0]
        
        for i in range(len(grid[0])):
            prefix.append(prefix[-1] + grid[1][i])
            
         
        
        for i in range(len(grid[0]) - 1, -1, -1):
            suffix[i] = suffix[i + 1] + grid[0][i]
                
            
        robot2= float("inf")
        
        for i in range(len(grid[0])):
            remain1 = suffix[i + 1]
            remain2 = prefix[i]
            ans = max(remain1, remain2)
            robot2 = min(robot2, ans)
            
        return robot2
            
            
            
            
            
            
            