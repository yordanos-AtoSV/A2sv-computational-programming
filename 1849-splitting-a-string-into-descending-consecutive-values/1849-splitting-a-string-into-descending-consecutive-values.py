class Solution:
    def splitString(self, s: str) -> bool:
        ans = []
        
        def back(idx):
            if idx >= len(s):
                return len(ans) >= 2
            
            for i in range(idx, len(s)):
                val = int(s[idx : i + 1])
                if len(ans) == 0 or ans[-1] - val == 1:
                    ans.append(val)
                    if back(i + 1):
                        return True
                    ans.pop()
                
            return False
        
        return back(0)    
            
        