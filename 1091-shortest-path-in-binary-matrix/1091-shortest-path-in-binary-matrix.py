class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return - 1
        direc = [(0,1), (0,-1), (1,0), (-1,0), (1, 1), (-1, 1), (1,-1), (-1, -1)]
        queue = deque()
        
        
        n = len(grid)
        
        inbound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid)
        level = 1    
      
        queue.append((0,0))
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                row , col = queue.popleft()
                
                if (row, col) == (n - 1, n - 1):
                    return level 
                
                for r, c in direc:
                    
                    nr = r + row
                    nc = c + col
                   
                    
                
                    if inbound(nr, nc) and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))
                        
            level += 1
                
        return -1
        