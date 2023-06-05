class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        
        def dp(row,idx):
            
            if row > len(triangle) - 1:
                return 0
            
         
            if (row, idx) not in memo:
                
                memo[(row, idx)] = min(dp(row + 1, idx) , dp(row + 1, idx + 1))
           
            return memo[(row, idx)] +  triangle[row][idx]
        
        
        return dp(0,0)