class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 :
            return 1
        
        bottomRow = [1] * n
        
        for i in range(m - 1):
            row = [1] * n 
            for j in range(n -2 , -1, -1):
                row[j] = bottomRow[j] + row[j + 1]
                
                
            bottomRow = row
            
            
        return row[0]