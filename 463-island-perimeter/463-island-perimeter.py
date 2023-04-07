class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1 , 0)]
        visited = [[0 for i in range (len(grid[0]))] for j in range (len(grid))]
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        count = 0 
        
        def recur(row, col):
            
            nonlocal count
            if visited[row][col] == False:
                
                visited[row][col] = True

                for rowchange, colchange in directions:
                    newrow = row + rowchange
                    newcol = col + colchange

                    if inbound(newrow, newcol) == False or grid[newrow][newcol] == 0:
                        count += 1
                    else:
                        recur(newrow , newcol)
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    recur(i, j)
                    
                    return count 
        