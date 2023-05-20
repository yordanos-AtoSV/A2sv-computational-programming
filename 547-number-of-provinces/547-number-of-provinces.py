class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
                
            return rep[x] 
        
        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep != yrep:
                if size[xrep] >= size[yrep]:
                    rep[yrep] = xrep
                    size[xrep] += size[yrep]
                    
                else:
                    rep[xrep] = yrep
                    size[yrep] += size[xrep] 
                    
        n = len(isConnected)   
        rep = {i : i for i in range(n )}
        size = {i : 1 for i in range(n)}
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and i != j:
                    
                    union(i , j)
                    
       
        parents = set()
        for i in range( n ):
            parents.add(find(i))
            
            
        return len(parents)
            
        