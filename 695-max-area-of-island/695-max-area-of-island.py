class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        visited = set()
        direc = [(0,1), (1, 0), (-1, 0), (0, -1)]
        
        def inbound(row, col):
            return 0 <= row <  len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col):
          
            if (row, col) not in visited and inbound(row, col) and  grid[row][col] != 0:
                visited.add((row, col))
  
                sum = 1
                for rows, cols in direc:
                  
                    new_row = rows + row
                    new_col = cols + col
           
                    
                    sum += dfs(new_row, new_col)
                    
                return sum
                
            else:
                return 0
                
                
        
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, dfs(i, j))

                
                
        return area