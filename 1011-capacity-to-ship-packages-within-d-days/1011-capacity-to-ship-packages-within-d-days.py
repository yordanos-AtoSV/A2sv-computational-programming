class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def capacity(cap):
            ships = 1
            capacity = cap
            for w in weights:
                if (capacity - w) < 0:
                    ships += 1
                    capacity = cap
                    
                capacity -= w
                
            return ships <= days
        
        
        l = max(weights)
        r = sum(weights)
        ans = r
        
        while l <= r :
            mid = (l + r) // 2
            if capacity(mid):
                ans = min(ans, mid)
                r = mid - 1
            else :
                l = mid + 1
                
        return ans