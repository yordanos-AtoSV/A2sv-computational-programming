class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans  = []
        p_count = Counter(p)
        window = Counter(s[:len(p)])
        
        for i in range(len(p), len(s)):
            
            if p_count == window:
                ans.append(i - len(p))
                
            window[s[i- len(p)]] -= 1
            
            if window[s[i- len(p)]] == 0:
                del window[s[i- len(p)]]
            
            window[s[i]] += 1
       
        if p_count == window:
            ans.append(len(s) - len(p)) 
        return ans
            
            
        