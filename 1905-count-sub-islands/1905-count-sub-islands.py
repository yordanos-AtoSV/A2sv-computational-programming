class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        count = 0
        directions = [(-1,0), (0, -1), (0, 1), (1, 0)]
        def inbound(row, col):
            return 0 <= row < len(grid2) and 0 <= col < len(grid2[0])
        flag = False
        def dfs( row,col):
            
            nonlocal flag    
            visited.add((row, col))
            
            for rows, cols in directions:
                new_row = row + rows
                new_col = col + cols
                
                if inbound(new_row, new_col) and (new_row, new_col) not in visited and grid2[new_row][new_col] !=0:
                    if grid1[new_row][new_col] == 1 :
                        dfs(new_row, new_col)
                    else:
                        flag = True
                        
                        
                        dfs(new_row, new_col)
                        
            return flag
                    
                    
                    
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i, j) not in visited and grid2[i][j] != 0 and grid1[i][j] == 1:
             
                   flag = False 
                     
                   ans = dfs( i, j)
        
                   if ans == False:
                     count += 1
 
             
        return count
        