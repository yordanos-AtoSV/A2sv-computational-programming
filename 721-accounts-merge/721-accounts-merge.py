class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
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
 
        
        rep = {i:i for i in range(len(accounts))}
        size = {i: 1 for i in range(len(accounts))}

        for i in range(len(accounts)):
            for j in range(i + 1, len(accounts)):
                val = len(set(accounts[i]).intersection(accounts[j])) 
                
                if val > 1:
                    union(i, j)
                                
        temp = []
        for i in range(len(accounts)):
            temp.append(find(i))
            
        res = defaultdict(list)
        
        for i in range(len(temp)):
            res[temp[i]].append(accounts[i])
            
        finres = []   
        for key, value in res.items():
            temp = []
            for email in value:
                name = email[0]
                temp += email[1:]
            temp = set(temp)   
            finres.append([name] + list(sorted(temp)))
            
        
        return finres    
            
    
  
    
        
        