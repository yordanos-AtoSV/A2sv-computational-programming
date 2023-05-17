class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        size = {i: 1 for i in range(n)}
        rep = {i:i for i in range(n)}
            
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
        
        
        def solution(source, destination):
            if destination == source:
                return True

            
            adjlist = defaultdict(list)

            for u, v in edges:
                adjlist[u].append(v) 
                adjlist[v].append(u)
                union(u, v)
            
            
            
            return connected(source, destination)

            
        return solution(source, destination)