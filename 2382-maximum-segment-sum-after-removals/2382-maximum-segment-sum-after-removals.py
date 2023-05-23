class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
                
            return rep[x] 
        
        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep != yrep:
                if rank[xrep] >= rank[yrep]:
                    
                    rep[yrep] = xrep
                    rank[xrep] += rank[yrep]
                    return rank[xrep]
                else:
                    rep[xrep] = yrep
                    rank[yrep] += rank[xrep] 
                    return rank[yrep]
                
            return rank[xrep]
                    
        n = len(nums)
        rep = {i:i for i in range(n)}
       
        rank = {i: nums[i] for i in range(n)}
        
        maxsum = 0
        ans = [0]
        temp = [0] * (n + 1)

        for i in range(n - 1 , - 1, -1):
            removed = removeQueries[i]
            temp[removed] = nums[removed]
            val = 0
            if temp[removed - 1] != 0 and temp[removed + 1] != 0:
                union(removed - 1, removed)
                val = union(removed, removed + 1)
             
                
            elif temp[removed -1] != 0 and temp[removed + 1] == 0:
                val = union(removed - 1, removed)
         
                
            elif temp[removed - 1] == 0 and temp[removed + 1] != 0:
                val = union(removed + 1, removed)
            
            else:
                val = union(removed, removed)
             
           
            maxsum = max(maxsum, val)
            ans.append(maxsum)
            
        return ans[::- 1][1:]
                
                