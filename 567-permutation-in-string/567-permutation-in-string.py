class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    s1_count = Counter(s1)
    window = Counter(s2[:len(s1) - 1])
    ans = False
    
    for i in range(len(s1) - 1, len(s2)):
        
             window[s2[i]] += 1
             if window == s1_count:
                ans = True 
               
        
             window[s2[i - len(s1) + 1]] -= 1
            
             if window[s2[i - len(s1) + 1]] == 0:
                del window[s2[i - len(s1) + 1]]
            
    return ans
          