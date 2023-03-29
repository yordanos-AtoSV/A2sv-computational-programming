class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            j = i
            count = 0
            one = 1
            while one <= j:
                temp = j & one
                if temp != 0:
                    count += 1
                    
                one = one << 1
                
            ans.append(count)
            
                    
        return ans
            
            
        