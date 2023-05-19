class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
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
             
        rep = {i: i for i in range(len(stones))}
        size = {i: 1 for i in range(len(stones))}
            
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                u, v = stones[i]
                u2, v2 = stones[j]
                if u == u2 or v == v2:
     
                    union(i, j)
        ans = []  
        for i in range(len(stones)):
            ans.append(find(i))
  
        ans = set(ans)
        return len(stones) - len(ans)
                
                
        