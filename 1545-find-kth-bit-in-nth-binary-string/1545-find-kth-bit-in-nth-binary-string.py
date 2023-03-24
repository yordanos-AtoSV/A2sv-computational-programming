class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def recur(i, s):
            if i == n:
           
                return s[k - 1]
            
            temp  = s + "1"
            
            inverse_s = ''

            for j in s:

                if j == '0':
                    inverse_s += '1'

                else:
                    inverse_s += '0'
                    
            temp = temp + inverse_s[::-1]
            
            return recur(i + 1, temp)
            
        return recur(1, "0")
        
    