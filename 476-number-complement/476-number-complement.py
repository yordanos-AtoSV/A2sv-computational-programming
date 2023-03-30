class Solution:
    def findComplement(self, num: int) -> int:
            x = bin(num)
            x = x[2:]
         
            ans = []
            for c in x :
                if c == "1":
                    ans.append("0")
                else:
                    ans.append("1")
                    
            ans = "".join(ans)
           
            return int(ans,2)
      
        