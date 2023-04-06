class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        path = []
        size = len(nums)
        sets = 0
        def recurs(sets, path):
            if len(path) == size:
                ans.append(path[:])
              
                return
            
            for i in range(len(nums)):
                temp = 1 << i
                ands = temp & sets
                if ands == 0:
                    sets |= temp
                    path.append(nums[i])
                    recurs(sets,path )
                    path.pop()
                    sets ^= temp
         
                else:
                    continue
                    
                    
                
        recurs(sets, path)
        
        return ans
    