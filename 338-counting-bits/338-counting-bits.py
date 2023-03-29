class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            j = i
            count = 0
            while j != 0:
                temp2 = j & 1
                if temp2 == 1:
                    count += 1
                j = j >> 1
                
            ans.append(count)
            
                    
        return ans
            
            
        