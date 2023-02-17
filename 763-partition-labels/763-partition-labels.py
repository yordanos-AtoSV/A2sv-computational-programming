class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i
            
        ans = []
        l = 0
        r = 0
        for i , c in enumerate(s):
            r = max(r, last_index[c])
            if i == r:
                ans.append(r - l +1)
                l = r + 1
                r += 1
        return ans
            
     
                
            
            
            
                
            
                
                
            
            
             
            
            
          
