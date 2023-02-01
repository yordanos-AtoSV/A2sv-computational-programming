class Solution:
    def largestMerge(self, a: str, b: str) -> str:
            ans = ""
            while a and b:
                if a > b:
                    ans += a[0]
                    a = a[1:]
                else:
                    ans += b[0]
                    b = b[1:]
       
            ans += a
            ans += b
            return ans




           
            
            
        
