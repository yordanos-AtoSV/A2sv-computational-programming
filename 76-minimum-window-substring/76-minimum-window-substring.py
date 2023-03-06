class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        count_t = {}
        
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
       
        l = 0 
        ans = [-1, -1]
        minsize = float("inf")
        have, need = 0, len(count_t)
            
        for r in range(len(s)):

            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1
                
            while have == need:
            
                if minsize > r - l + 1:
                    minsize = r - l + 1
                    ans = [l, r]
            
                window[s[l]] -= 1

                    
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                
                    have -= 1
                   
                l += 1
              
                
        l, r = ans  

        if minsize != float(inf):
            return s[l:r + 1]

        else:
            return ""
       
    
    