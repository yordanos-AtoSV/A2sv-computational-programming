class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        path = []
        size = len(nums)
        sets = []
        def recurs(sets, path):
            if len(path) == size:
                ans.append(path[:])
              
                return
            
            for i in range(len(nums)):
                if nums[i] in sets:
                    continue
                else:
                    sets.append(nums[i])
                    path.append(nums[i])
                    recurs(sets,path )
                    path.pop()
                    sets.pop()
         
                    
                
        recurs(sets, path)
        
        return ans
    