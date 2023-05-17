class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = {i: i for i in range(1, len(edges) + 1)}
        size = {i: 1 for i in range(1, len(edges) + 1)}
        
        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
                
            return rep[x]
        
        def union(x, y, ans):
            xrep = find(x)
            yrep = find(y)
            
            if xrep != yrep:
                if size[xrep] > size[yrep]:
                    rep[yrep] = xrep
                    size[xrep] += size[yrep]
                else:
                    rep[xrep] = yrep
                    size[yrep] += size[xrep]
                    
            else:
                ans[0] = x
                ans[1] = y
            
        def solution(edges):
            ans = [-1, - 1]
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
                union(u, v, ans)
                
            return ans
            
        return solution(edges)