class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        size = {i: 1 for i in range(1 ,  n + 1)}
        rep = {i:i for i in range(1, n + 1)}
            
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
                        
        def connected(x, y):
                return find(x) == find(y)
        
        
        def solution(n, roads):

            for u, v, w in roads:
                union(u, v)
            ans = float("inf")  
            for u , v , w in roads:
                if connected(1, u):
                    ans = min(ans, w)
            
            
            
            return ans

            
        return solution(n, roads)
        
#         rep = {i : [i, float("inf")] for i in range(1, n + 1 )}
#         size = {i : 1 for i in range(1, n + 1)}
        
#         def find(x):
#             if rep[x][0] != x:
#                 rep[x][0] = find(rep[x][0])
                
#             return rep[x][0]
        
#         def union(x, y, w):
#             xrep = find(x)
#             xw = rep[xrep][1]
#             yrep = find(y)
#             yw = rep[yrep][1]
            
#             if xrep != yrep:
#                 if size[xrep] >= size[yrep]:
#                     rep[yrep] = xrep
#                     size[xrep] += size[yrep]
#                     rep[xrep][1] = min(xw, w, yw)
                        
#                 else:
                    
#             else:
                
                        
                    
#         def solution(n , roads):
   
#             for u, v, w in roads:
#                 union(u, v, w)
            
#             ans = find(1)
#             return rep[ans][1]
    
#         return solution(n , roads)