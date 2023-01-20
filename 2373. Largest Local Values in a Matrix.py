class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        length = len(grid)-2
        for index in range(length):
            row_val = ['0'] * length
            ans.append(row_val)
        

        m = 0
        for i in range((len(grid)-3) +1):
            l = 0
            for p in range((len(grid)-3) +1):
                max=0
                for j in range(3):
                    for k in range(3):
                        
                        if grid[j + m][k + l] > max:
                            max = grid[j + m][k + l]
                            
                ans[i][p] = max
               
                l +=1
            m += 1
       
        return ans
