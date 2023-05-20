class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
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
                    
        check = set(nums)
        nums = list(set(nums))
        n = len(nums)
        if not nums:
            return 0
        
        rep = {nums[i] :nums[i] for i in range(n)}
        size = {nums[i]: 1 for i in range(n)}
        n = len(nums)
        for i in range(n):
            x1 = nums[i] + 1
            x2 = nums[i] - 1
            if x1 in check:
                union(x1, nums[i])
            if x2 in check:
                union(x2, nums[i])
                
        parents = Counter()
        for i in range(n):
            parent = find(nums[i])
            parents[parent] += 1
            
            
        return max(parents.values())