class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:    
            
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
        
        n = len(source)
        size = {i: 1 for i in range(n)}
        rep = {i:i for i in range(n)}
       
        for u , v in allowedSwaps :
            union(u , v)
                   
        m = {}
        for i in range(n):
            row = find(i)
            if row not in m:
                m[row] = {}
            m[row][source[i]] = m[row].get(source[i], 0) + 1

        for i in range(n):
            row = find(i)
            if row not in m:
                m[row] = {}
            m[row][target[i]] = m[row].get(target[i], 0) - 1
            
     
        ans = 0
        for row in m.values():
            for val in row.values():
                ans += abs(val)

        return ans // 2
            
    