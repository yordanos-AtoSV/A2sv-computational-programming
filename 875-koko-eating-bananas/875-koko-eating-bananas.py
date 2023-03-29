class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            count = 0
            mid = (l + r) // 2
            for c in piles:
                check = math.ceil(c / mid)
                count += check
                
            if count <= h:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
                
        return ans
                
            