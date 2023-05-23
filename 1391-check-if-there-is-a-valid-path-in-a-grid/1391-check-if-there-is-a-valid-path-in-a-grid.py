class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def find(x):
            if rep[x] != x:
                rep[x]= find(rep[x])
                
            return rep[x]

        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            if xrep != yrep:
                if size[xrep] > size[yrep]:   
                    rep[yrep] = xrep
                    size[xrep] += size[yrep]
                else:
                    rep[xrep] = yrep
                    size[yrep] += size[xrep]
                    
        def inbound(row , col):
            nonlocal n
            nonlocal m
            return 0 <= row < n and 0 <= col < m 
        
        n = len(grid)
        m = len(grid[0])
        
        size = {(i,j): 1 for i in range(n) for j in range(m)}
        rep = {(i, j):(i, j) for i in range(n) for j in range(m)}
        
        roadmap = {1:[(),(3, 1, 5)], 2:[(5,2,6),()], 3:[(5, 6, 2),()], 4:[(5,6,2),(1,5,3)], 5:[(),()], 6:[(),(1,5,3)]}

        for i in range(n):
            for j in range(m):
                street = grid[i][j]

                row = i + 1
                if inbound(row, j):
                    v = grid[row][j]
                    if v in roadmap[street][0]:
                        union((i, j), (row, j))
                        
                col = j + 1
                if inbound(i, col):
                    h = grid[i][col]
          
                    if h in roadmap[street][1]:
                        union((i, col), (i, j))
   
        return find((0, 0)) == find((n - 1, m - 1))
        