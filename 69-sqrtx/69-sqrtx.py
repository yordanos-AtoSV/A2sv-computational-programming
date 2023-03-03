class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        low = -1 
        high = x + 1

        
        while low + 1 < high:
            mid = low + (high - low) // 2
     
            if mid * mid < x:
                ans = mid
                low = mid 
                
            elif mid * mid > x:
                high = mid 
  

            else:
                ans = mid
                break
                  
        return ans 
        