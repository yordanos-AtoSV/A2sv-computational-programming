class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
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
        rep = {i:i for i in range(len(s))}
        size = {i: 1 for i in range(len(s))}
        
        for u, v in pairs:
            union(u, v)
            
        temp = []
        for i in range(len(s)):
            temp.append(find(i))
            
        ans = defaultdict(list)
        for i in range(len(temp)):
            ans[temp[i]].append((s[i], i))
        result = ["0"] * len(s)    
        for key, value in ans.items():
            index = []
            temp = sorted(value, key=lambda x: x[0])
            for w, i in temp:
                index.append(i)
            index.sort()
            p = 0
            for w, i in temp:
               
                result[index[p]] = w
                p += 1
       
            

        return "".join(result)