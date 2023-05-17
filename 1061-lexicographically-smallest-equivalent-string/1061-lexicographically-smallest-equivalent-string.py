class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {i: i for i in range(ord("a"), ord("a") + 26)}
        ans = [] 
  
        
        def find(x):
            if rep[ord(x)] != ord(x):
                rep[ord(x)] = find(chr(rep[ord(x)]))
            
            return rep[ord(x)]
        
        
        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep != yrep:
                if xrep < yrep:
                    rep[yrep] = xrep
                else:
                    rep[xrep] = yrep
            
            
        
        def solution(s1, s2, basestr):
            p1, p2 = 0, 0
            for _ in range(len(s1)):
                union(s1[p1], s2[p2])
                p1 += 1 
                p2 += 1
                
            for s in basestr:
                ch = chr(find(s))
       
                ans.append(ch)
      
        
            return "".join(ans)
        
        return solution(s1, s2, baseStr)
            