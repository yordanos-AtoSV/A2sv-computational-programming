# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = -1 
        high = n + 1
        i = 0
        
        while low + 1 < high:
            mid = low + (high - low) // 2
            
            if isBadVersion(mid) == True:
                high = mid 
            if isBadVersion(mid) == False:
                low = mid 
            
                
        return high
        