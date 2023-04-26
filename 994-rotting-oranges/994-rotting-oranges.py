class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direc = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])   
            
        ans = 0    
        count = 0
        queue = deque()
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        count += 1
                    if grid[i][j] == 2:
                        queue.append((i, j))
                        
                        
                        
        while queue and count > 0:
            
            ans += 1
            
            for i in range(len(queue)):
                
                r, c = queue.popleft()
                
                for row , col in direc:
                    nr = r + row
                    nc = c + col
                    
                    if  inbound(nr,nc) and grid[nr][nc] == 1:
                       
                        count -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                    
                    
        return ans if count == 0 else -1 
                
                        
                    
                
                
        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                