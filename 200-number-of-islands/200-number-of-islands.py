class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for _ in range (len(grid[0]))] for _ in range (len(grid))]
        ans = 0
                                      
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])                        
                                      
        def recur(row, col):
                                      
            
            visited[row][col] = True
            for newrow, newcol in directions:
                    new_row = row + newrow
                    new_col = col + newcol
                                      
                    if inbound(new_row, new_col) and not visited[new_row][new_col]:
                        if grid[new_row][new_col] == "1":
                                      recur(new_row, new_col)
          
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                   if inbound(i, j) and not visited[i][j] and grid[i][j] == "1":
                        
                        ans += 1
                        recur(i ,j )       
        return ans
                                      
                                                                      
        