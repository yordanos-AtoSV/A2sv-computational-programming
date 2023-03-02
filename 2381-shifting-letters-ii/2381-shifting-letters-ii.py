class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        size = len(s) + 1
        temp_arr = [0] * size 
        for start, end , d in  shifts:
            if d == 0:
                temp_arr[start] += -1
                temp_arr[end + 1] += 1
            else:
                temp_arr[start] += 1
                temp_arr[end + 1] += -1 
                
        pref_sum = []
        prev = 0
        for i in range(len(temp_arr) - 1):
            prev += temp_arr[i]
            pref_sum.append(prev)
        ans = []
        for i in range(len(s)):
            temp =( ord(s[i]) -ord("a") + pref_sum[i] )% 26  
            x = temp +ord("a")
            ans.append(chr(x))
            
        return "".join(ans)
            

                
                    
            
                
            
        
            
        
      
        for i in range(len(s)):
            print(ord(s[i]))
            print(chr(ord(s[i]) + 1))